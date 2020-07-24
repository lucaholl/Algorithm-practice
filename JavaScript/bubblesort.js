const bubbleSort = arr => {
    let swapCount = 1;
    
    while (swapCount > 0) {
      swapCount = 0;
      for (let i = 0; i < arr.length - 1; i++) {
        if (arr[i] > arr[i + 1]) {
          let tmp = arr[i];
          arr[i] = arr[i + 1];
          arr[i + 1] = tmp;
          swapCount++;
        }
      }
    }
    return arr;
  };

export default bubbleSort;