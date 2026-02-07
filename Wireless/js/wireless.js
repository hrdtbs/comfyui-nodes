import { app } from "../../scripts/app.js";

app.registerExtension({
	name: "h2nodes.Wireless",
	async setup() {
		// Store original graphToPrompt to call it later
		const originalGraphToPrompt = app.graphToPrompt;

		app.graphToPrompt = async function () {
			// Call original function first to get the initial prompt structure
			const result = await originalGraphToPrompt.apply(this, arguments);

			// Handle different return structures (some versions return object with output, some return prompt directly)
			let prompt = result.output || result;
            if (!prompt) return result;

			// Find all Wireless nodes in the current graph
			const wirelessNodes = app.graph.findNodesByType("Wireless");
			if (!wirelessNodes || wirelessNodes.length === 0) return result;

            // Sort wireless nodes by position (top-to-bottom, then left-to-right)
            // This ensures "last processed" aligns with visual flow
            wirelessNodes.sort((a, b) => {
                if (a.pos[1] !== b.pos[1]) {
                    return a.pos[1] - b.pos[1]; // Sort by Y (vertical)
                }
                return a.pos[0] - b.pos[0]; // Sort by X (horizontal) as secondary
            });

			// Map to store available sources:
			// sources[TYPE] = [ { name: "SLOT_NAME", link: [NodeID, SlotIndex] }, ... ]
			const sources = {};

			// 1. Identify sources from Wireless nodes
			for (const node of wirelessNodes) {
				// Check if the first input exists and has a link
				if (node.inputs && node.inputs[0] && node.inputs[0].link) {
					const linkId = node.inputs[0].link;
					const link = app.graph.links[linkId];
					if (!link) continue;

					const originNode = app.graph.getNodeById(link.origin_id);
					if (!originNode) continue;

					const originSlot = originNode.outputs[link.origin_slot];
					if (!originSlot) continue;

					const type = originSlot.type;
					const slotName = originSlot.name;

					// Skip generic types ("*") to avoid broad broadcasting
					if (!type || type === "*") continue;

					if (!sources[type]) {
						sources[type] = [];
					}

					// Store source info: link data and the name of the output slot
					sources[type].push({
						name: slotName,
						link: [String(link.origin_id), parseInt(link.origin_slot)]
					});
				}
			}

			// 2. Inject into prompt
			for (const nodeId in prompt) {
				const nodeData = prompt[nodeId];

                // Skip special node types or undefined data
                if (!nodeData || !nodeData.class_type) continue;

				// Skip Wireless nodes themselves
				if (nodeData.class_type === "Wireless") continue;

				// Get the actual graph node object to inspect its inputs
				const node = app.graph.getNodeById(nodeId);
				if (!node || !node.inputs) continue;

				// Iterate over inputs of the target node
				for (const input of node.inputs) {
					const inputName = input.name;
					const inputType = input.type;

					// Skip if input type is generic or unknown
					if (!inputType || inputType === "*") continue;

					// Check if this input is already connected in the prompt (has a link)
					if (nodeData.inputs && nodeData.inputs[inputName] !== undefined) {
						continue; // Already connected or has value
					}

					// Find matching sources based on type
					let potentialSources = [];

                    // Handle array types (e.g. valid connection types) vs single string type
					if (Array.isArray(inputType)) {
						for (const t of inputType) {
							if (sources[t]) {
								potentialSources = potentialSources.concat(sources[t]);
							}
						}
					} else {
						if (sources[inputType]) {
							potentialSources = sources[inputType];
						}
					}

					if (potentialSources.length > 0) {
						let bestMatch = null;

						// Priority 1: Match by name (case-insensitive)
                        // Iterate through all potential sources to find a name match
						for (const source of potentialSources) {
							if (source.name && inputName && source.name.toLowerCase() === inputName.toLowerCase()) {
								bestMatch = source.link;
                                // If multiple name matches exist, we take the last one encountered (due to loop order)
                                // which corresponds to "last processed" requirement if sources are ordered.
							}
						}

						// Priority 2: If no name match, use the last available source of the correct type
						if (!bestMatch) {
							const lastSource = potentialSources[potentialSources.length - 1];
							bestMatch = lastSource.link;
						}

						// Apply the connection
						if (bestMatch) {
							if (!nodeData.inputs) nodeData.inputs = {};
							nodeData.inputs[inputName] = bestMatch;
						}
					}
				}
			}

			return result;
		};
	},
});
