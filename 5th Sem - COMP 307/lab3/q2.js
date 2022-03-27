let memoryFrame = [];
// const pageQueue = [7, 2, 3, 1, 2, 5, 3, 4, 6, 7, 7, 1, 0, 5, 4, 6, 2, 3, 0, 1];
const pageQueue = [
	1, 0, 2, 2, 1, 7, 6, 7, 0, 1, 2, 0, 3, 0, 4, 5, 1, 5, 2, 4, 5, 6, 7, 6, 7, 2, 4, 2, 7, 3, 3, 2,
	3,
];

let remainingQueue = [...pageQueue];

let hitsMisses = [];
let pageFaults = 0;

/**
 * First IN First Out Replacement
 * @param {array} memoryFrame
 * @param {array} pageQueue
 * @param {int} capacity
 */
const fifo = (memoryFrame, pageQueue, capacity) => {
	// iterate pages
	pageQueue.forEach((page, i) => {
		// check memory frame empty
		if (memoryFrame.length === 0) {
			memoryFrame[i] = [{ page: page, entryIndex: i }];
			pageFaults += 1;
			hitsMisses[i] = "miss";
		}
		// check memory frame filled
		else {
			if (memoryFrame[i].length < capacity) {
				// check matching
				hit = memoryFrame[i].some((segment) => segment.page === page);
				// if matching ie hit
				if (hit) hitsMisses[i] = "hit";
				// else replace
				else {
					memoryFrame[i].push({ page: page, entryIndex: i });
					pageFaults += 1;
					hitsMisses[i] = "miss";
				}
			}

			// check previous memory frame for hit then replace
			else if (memoryFrame[i].length === capacity) {
				// check matching
				hit = memoryFrame[i].some((segment) => segment.page === page);
				// if matching ie hit
				if (hit) hitsMisses[i] = "hit";
				// else replace
				else {
					lowestEntry = null;
					earliestIndex = null;

					memoryFrame[i].forEach((segment, index) => {
						if (lowestEntry === null || segment.entryIndex < lowestEntry) {
							lowestEntry = segment.entryIndex;
							earliestIndex = index;
						}
					});

					pageFaults += 1;
					memoryFrame[i][earliestIndex] = { page: page, entryIndex: i }; //replacing first
					hitsMisses[i] = "miss";
					lowestEntry = null;
					earliestIndex = null;
				}
			}
		}

		// copy current index to next index for saving state and easy replacement
		if (i < pageQueue.length - 1) memoryFrame[i + 1] = [...memoryFrame[i]];
	});

	let newTable = [];
	memoryFrame.forEach((segment, i) => {
		let frame = [];
		for (i = 0; i < capacity; i++) {
			if (segment[i]) frame[i] = segment[i].page;
			else frame[i] = null;
		}

		newTable.push({
			frame1: frame[0],
			frame2: frame[1],
			frame3: frame[2],
			frame4: frame[3],
			hitOrMiss: hitsMisses[memoryFrame.indexOf(segment)],
		});
	});

	console.table(newTable);
	console.log("Page Faults = ", pageFaults);
};

/**
 * Least Recently Used Replacement
 * @param {array} memoryFrame
 * @param {array} pageQueue
 * @param {int} capacity
 */
const lru = (memoryFrame, pageQueue, capacity) => {
	// iterate pages
	pageQueue.forEach((page, i) => {
		// check memory frame empty
		if (memoryFrame.length === 0) {
			memoryFrame[i] = [{ page: page, accessIndex: i }];
			pageFaults += 1;
			hitsMisses[i] = "miss";
		}
		// check memory frame filled
		else {
			if (memoryFrame[i].length < capacity) {
				// check matching
				hit = memoryFrame[i].some((segment) => segment.page === page);
				// if matching ie hit, update previously existing's access to current
				if (hit) {
					hitIndex = memoryFrame[i].findIndex((segment) => segment.page === page);
					memoryFrame[i][hitIndex].accessIndex = i;
					hitsMisses[i] = "hit";
				} else {
					memoryFrame[i].push({ page: page, accessIndex: i });
					pageFaults += 1;
					hitsMisses[i] = "miss";
				}
			}

			// check previous memory frame for hit then replace
			else if (memoryFrame[i].length === capacity) {
				// check matching
				hit = memoryFrame[i].some((segment) => segment.page === page);
				// if matching ie hit, update previously existing's access to current
				if (hit) {
					hitIndex = memoryFrame[i].findIndex((segment) => segment.page === page);
					memoryFrame[i][hitIndex].accessIndex = i;
					hitsMisses[i] = "hit";
				}
				// else replace
				else {
					lowestEntry = null;
					earliestIndex = null;

					memoryFrame[i].forEach((segment, index) => {
						if (lowestEntry === null || segment.accessIndex < lowestEntry) {
							lowestEntry = segment.accessIndex;
							earliestIndex = index;
						}
					});

					pageFaults += 1;
					memoryFrame[i][earliestIndex] = { page: page, accessIndex: i }; //replacing first
					hitsMisses[i] = "miss";
					lowestEntry = null;
					earliestIndex = null;
				}
			}
		}

		// copy current index to next index for saving state and easy replacement
		if (i < pageQueue.length - 1) memoryFrame[i + 1] = [...memoryFrame[i]];
	});

	let newTable = [];
	memoryFrame.forEach((segment, i) => {
		let frame = [];
		for (i = 0; i < capacity; i++) {
			if (segment[i]) frame[i] = segment[i].page;
			else frame[i] = null;
		}

		newTable.push({
			frame1: frame[0],
			frame2: frame[1],
			frame3: frame[2],
			frame4: frame[3],
			hitOrMiss: hitsMisses[memoryFrame.indexOf(segment)],
		});
	});

	console.table(newTable);
	console.log("Page Faults = ", pageFaults);
};

/**
 * Optimal Replacement
 * @param {array} memoryFrame
 * @param {array} pageQueue
 * @param {int} capacity
 */
const optimal = (memoryFrame, pageQueue, capacity) => {
	// iterate pages
	pageQueue.forEach((page, i) => {
		remainingQueue.shift();

		// check next access
		let nextAccessIndex = remainingQueue.findIndex((x) => x === page);
		if (nextAccessIndex !== -1) nextAccessIndex = i + 1 + nextAccessIndex;
		else if (nextAccessIndex === -1) nextAccessIndex = null;

		// when memory frame empty
		if (memoryFrame.length === 0) {
			memoryFrame[i] = [{ page: page, nextAccessIndex: nextAccessIndex }];
			pageFaults += 1;
			hitsMisses[i] = "miss";
		}
		// when memory frame filled
		else {
			// when not completely flled
			if (memoryFrame[i].length < capacity) {
				memoryFrame[i].push({ page: page, nextAccessIndex: nextAccessIndex });
				pageFaults += 1;
				hitsMisses[i] = "miss";
			}

			// when completely
			else if (memoryFrame[i].length === capacity) {
				// check matching
				hit = memoryFrame[i].some((segment) => segment.page === page);
				// if matching ie hit, update matching's next access
				if (hit) {
					hitIndex = memoryFrame[i].findIndex((segment) => segment.page === page);
					memoryFrame[i][hitIndex].nextAccessIndex = nextAccessIndex;
					hitsMisses[i] = "hit";
				}
				// if not mathcing  replace
				else {
					let highestEntry = memoryFrame[i][0].nextAccessIndex;
					let ultimateIndex = 0;

					memoryFrame[i].forEach((segment, index) => {
						// when null, higher priority null
						if (segment.nextAccessIndex === null) {
							ultimateIndex = index;
						}
						// when not null and greater
						else if (segment.nextAccessIndex > highestEntry) {
							highestEntry = segment.nextAccessIndex;
							ultimateIndex = index;
						}
					});

					pageFaults += 1;
					memoryFrame[i][ultimateIndex] = {
						page: page,
						nextAccessIndex: nextAccessIndex,
					}; //replacing first
					hitsMisses[i] = "miss";
					highestEntry = null;
					ultimateIndex = null;
				}
			}
		}

		// copy current index to next index for saving state and easy replacement
		if (i < pageQueue.length - 1) memoryFrame[i + 1] = [...memoryFrame[i]];
	});

	let newTable = [];
	memoryFrame.forEach((segment, i) => {
		let frame = [];
		for (i = 0; i < capacity; i++) {
			if (segment[i]) frame[i] = segment[i].page;
			else frame[i] = null;
		}

		newTable.push({
			frame1: frame[0],
			frame2: frame[1],
			frame3: frame[2],
			frame4: frame[3],
			hitOrMiss: hitsMisses[memoryFrame.indexOf(segment)],
		});
	});

	console.table(newTable);
	console.log("Page Faults = ", pageFaults);
};

/**
 * Second Chance Replacement
 * @param {array} memoryFrame
 * @param {array} pageQueue
 * @param {int} capacity
 */
const second = (memoryFrame, pageQueue, capacity) => {
	// iterate pages
	pageQueue.forEach((page, i) => {
		// check memory frame empty
		if (memoryFrame.length === 0) {
			memoryFrame[i] = [{ page: page, entryIndex: i, chance: 0 }];
			pageFaults += 1;
			hitsMisses[i] = "miss";
		}
		// check memory frame filled
		else {
			if (memoryFrame[i].length < capacity) {
				hit = memoryFrame[i].findIndex((segment) => segment.page === page);
				// if matching ie hit
				if (hit !== -1) {
					hitsMisses[i] = "hit";
					memoryFrame[i][hit].chance = 1;
				}
				// if miss
				else {
					memoryFrame[i].push({ page: page, entryIndex: i, chance: 0 });
					pageFaults += 1;
					hitsMisses[i] = "miss";
				}
			}

			// check previous memory frame for hit then replace
			else if (memoryFrame[i].length === capacity) {
				// check hit
				hit = memoryFrame[i].findIndex((segment) => segment.page === page);
				// if matching ie hit
				if (hit !== -1) {
					hitsMisses[i] = "hit";
					memoryFrame[i][hit].chance = 1;
				}
				// else replace
				else {
					let pageToReplace = null;
					let tempSegment = [...memoryFrame[i]];

					while (pageToReplace === null) {
						let lowestEntry = tempSegment[0].entryIndex;
						let earliestIndex = 0;

						// find earliest index
						tempSegment.forEach((segment, index) => {
							if (segment.entryIndex < lowestEntry) {
								lowestEntry = segment.entryIndex;
								earliestIndex = index;
							}
						});

						// check chance
						// if no chance, replace
						if (tempSegment[earliestIndex].chance === 0) {
							pageToReplace = tempSegment[earliestIndex].page;
						}
						// if chance , remove chance then find next earliest
						else if (tempSegment[earliestIndex].chance === 1) {
							memoryFrame[i][earliestIndex].chance = 0;
							tempSegment.splice(earliestIndex, 1);
						}

						lowestEntry = null;
						earliestIndex = null;
					}

					pageFaults += 1;
					let indexToReplace = memoryFrame[i].findIndex((x) => x.page == pageToReplace);

					// check chance before replacing

					memoryFrame[i][indexToReplace] = { page: page, entryIndex: i, chance: 0 }; //replacing first
					hitsMisses[i] = "miss";
				}
			}
		}

		// copy current index to next index for saving state and easy replacement
		if (i < pageQueue.length - 1) memoryFrame[i + 1] = [...memoryFrame[i]];
	});

	let newTable = [];
	memoryFrame.forEach((segment, i) => {
		let frame = [];
		for (i = 0; i < capacity; i++) {
			if (segment[i]) frame[i] = segment[i].page;
			else frame[i] = null;
		}

		newTable.push({
			frame1: frame[0],
			frame2: frame[1],
			frame3: frame[2],
			frame4: frame[3],
			hitOrMiss: hitsMisses[memoryFrame.indexOf(segment)],
		});
	});

	console.table(newTable);
	console.log("Page Faults = ", pageFaults);
};

// driver
// fifo(memoryFrame, pageQueue, 3);
lru(memoryFrame, pageQueue, 4);
// optimal(memoryFrame, pageQueue, 3);
// second(memoryFrame, pageQueue, 3);
