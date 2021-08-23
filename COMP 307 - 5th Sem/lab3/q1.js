const _memoryPartitions = [
	{
		size: 300,
		occupied: 0,
		remaining: 300,
	},
	{
		size: 600,
		occupied: 0,
		remaining: 600,
	},
	{
		size: 350,
		occupied: 0,
		remaining: 350,
	},
	{
		size: 200,
		occupied: 0,
		remaining: 200,
	},
	{
		size: 750,
		occupied: 0,
		remaining: 750,
	},
	{
		size: 125,
		occupied: 0,
		remaining: 125,
	},
];

const _pages = [
	{
		size: 115,
		allocated: false,
		block: null,
	},
	{
		size: 500,
		allocated: false,
		block: null,
	},
	{
		size: 358,
		allocated: false,
		block: null,
	},
	{
		size: 200,
		allocated: false,
		block: null,
	},
	{
		size: 375,
		allocated: false,
		block: null,
	},
];

let firstFit = (memoryPartitions, pages) => {
	console.log(
		"\n-----------------------------------\n\tFIRST FIT\n-----------------------------------\n"
	);

	// iterate each page objects
	for (page of pages) {
		// iterate each memory partiton
		for (partition of memoryPartitions) {
			// check given page can fit in memory partition
			if (page.size <= partition.remaining) {
				page.allocated = true;
				page.block = partition.size;
				partition.occupied += page.size;
				partition.remaining -= page.size;
				break; // immediately exit loop after first fitting partition is found
			}
		}
	}
	console.table(pages); // display pages

	let freeMemory = 0;

	// iterate through partitions to check free memory
	for (partition of memoryPartitions) {
		if (partition.occupied != 0) {
			freeMemory += partition.remaining;
		}
	}

	console.log("Free memory in occupied partitions = ", freeMemory);
	console.table(memoryPartitions);
};

let bestFit = (memoryPartitions, pages) => {
	console.log(
		"\n-----------------------------------\n\tBEST FIT\n-----------------------------------\n"
	);

	let previousFit = null; // variable for storing fit partition for comparision
	//iterate page objects
	for (let page of pages) {
		// iterate parition objects
		for (let partition of memoryPartitions) {
			// check fit
			if (page.size <= partition.remaining) {
				let currentFit = memoryPartitions.indexOf(partition);
				// initial assignment of first fit
				if (previousFit == null) previousFit = currentFit;
				// if already available for comparision, check best fit by comparing
				else if (
					page.size <= memoryPartitions[currentFit].size &&
					memoryPartitions[currentFit].size < memoryPartitions[previousFit].remaining
				)
					previousFit = currentFit;
			}
		}
		// after obtaining best fit allocate to pages accordingly
		if (previousFit != null) {
			page.allocated = true;
			page.block = memoryPartitions[previousFit].size;
			memoryPartitions[previousFit].occupied += page.size;
			memoryPartitions[previousFit].remaining -= page.size;
		}
		previousFit = null;
	}

	console.table(pages);

	let freeMemory = 0;
	// check free memory
	for (partition of memoryPartitions) {
		if (partition.occupied != 0) {
			freeMemory += partition.remaining;
		}
	}

	console.log("Free memory in occupied partitions = ", freeMemory);
};

let worstFit = (memoryPartitions, pages) => {
	console.log(
		"\n-----------------------------------\n\tWORST FIT\n-----------------------------------\n"
	);

	let previousFit = null;
	for (let page of pages) {
		for (let partition of memoryPartitions) {
			if (page.size <= partition.remaining) {
				let currentFit = memoryPartitions.indexOf(partition);
				if (previousFit == null) previousFit = currentFit;
				else if (
					page.size <= memoryPartitions[currentFit].size &&
					memoryPartitions[currentFit].size > memoryPartitions[previousFit].remaining
				)
					previousFit = currentFit;
			}
		}

		if (previousFit != null) {
			page.allocated = true;
			page.block = memoryPartitions[previousFit].size;
			memoryPartitions[previousFit].occupied += page.size;
			memoryPartitions[previousFit].remaining -= page.size;
		}

		previousFit = null;
	}

	console.table(pages);

	let freeMemory = 0;

	for (partition of memoryPartitions) {
		if (partition.occupied != 0) {
			freeMemory += partition.remaining;
		}
	}

	console.log("Free memory in occupied partitions = ", freeMemory);
};

firstFit(_memoryPartitions, _pages);
bestFit(_memoryPartitions, _pages);
worstFit(_memoryPartitions, _pages);
