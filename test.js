function steamrollArray(arr) {
  let newArr = [];

  function recursive(arr) {
    if (Array.isArray(arr)) {
      for (let i in arr) {
        recursive(arr[i]);
      }
    } else newArr.push(arr);
  }

  recursive(arr);
  console.log(newArr);
  return newArr;
}

/*
 * @param {number[]} nums
 * @return {number[]}
 */

var productExceptSelf = function (nums) {
  const newArr = [1]; //siempre el primero va a ser uno cuando calcule los pre
  const length = nums.length;
  let temp = 1;

  for (let i = 1; i < length; i++) {
    newArr.push(temp * nums[i - 1]);
    temp *= nums[i - 1];
  }

  temp = nums[length - 1];

  for (let i = length - 1; i > 0; i--) {
    newArr[i - 1] *= temp;
    temp *= nums[i - 1];
  }

  return newArr;
};

/*
 * @param {character[][]} board
 * @return {boolean}
 */
var isValidSudoku = function (board) {
  let result = true;
  let sector = 1;
  let index = new Map();

  //recopilamos coordenadas
  //sector, hor, ver

  board.map((a, b) => {
    for (let i in a) {
      //routeado basico de sectores, y reseteo
      switch (b) {
        case 0:
        case 1:
        case 2:
          if (i == "0") sector = 1;
          break;
        case 3:
        case 4:
        case 5:
          if (i == "0") sector = 4;
          break;
        case 6:
        case 7:
        case 8:
          if (i == "0") sector = 7;
          break;
      }

      if (i == "3") sector++;
      if (i == "6") sector++;

      if (a[i] == ".") continue;
      //+ 1 porque arrancan en 0
      //la idea es separar en 3 array uno por cada coordenada para luego filtar repetidos
      if (index.get(a[i])) {
        index.get(a[i])[0].push(sector);
        index.get(a[i])[1].push(parseInt(i) + 1);
        index.get(a[i])[2].push(b + 1);
      } else index.set(a[i], [[sector], [parseInt(i) + 1], [b + 1]]);
    }
  });

  const results = [...index.values()];

  for (let i in results) {
    for (let j in results[i]) {
      index = new Map();
      results[i][j].map((a) => {
        if (index.get(a)) result = false;
        else index.set(a, 1);
      });
      if (!result) break;
    }
    if (!result) break;
  }
  return result;
};

var encodeDecode = function (arr, decode = false) {
  if (decode) arr = arr[0].split("$");

  arr = arr.map((word) => {
    let newStr = "";
    for (let i in word) {
      if (decode) newStr += String.fromCharCode(word[i].charCodeAt() - 125);
      else newStr += String.fromCharCode(word[i].charCodeAt() + 125);
    }

    return (word = newStr);
  });

  if (decode) return arr;
  return [arr.join("$")];
};

/*
 * @param {number[]} nums
 * @return {number}
 */
var longestConsecutive = function (nums) {
  if (!nums) return 0;
  let longest = 1;
  let current = 1;

  nums.sort((a, b) => a - b);

  for (let i = 0; i < nums.length - 1; i++) {
    if (nums[i] == nums[i + 1]) continue;
    if (nums[i] + 1 == nums[i + 1]) current++;
    else current = 1;
    if (current > longest) longest = current;
  }

  return longest;
};

var isPalindrome = function (s) {
  s = s.replace(/[^A-Za-z0-9]/g, "").toLowerCase();
  let end = s.length - 1;
  let beg = 0;

  while (beg != end) {
    if (s[beg] === s[end]) {
      beg++;
      end--;
      continue;
    }
    return false;
  }

  return true;
};

var twoSum = function (numbers, target) {
  let end = numbers.length - 1;
  let beg = 0;

  while (beg != end) {
    let current = target - numbers[beg];
    if (current < numbers[end]) end--;
    else if (current === numbers[end]) break;
    else beg++;
  }

  return [numbers[beg], numbers[end]];
};

/*Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.*/

/*
 * @param {number[]} nums
 * @return {number[][]}
 */
var threeSum = function (nums) {
  nums.sort((a, b) => a - b);
  let triplets = [];

  for (let i = 0; i < nums.length - 2; i++) {
    const tempArr = nums.slice(i);
    console.log(tempArr);

    //console.log(twoSum(nums[i]))
  }

  return nums;
};

console.log(threeSum([-1, 0, 1, 2, -1, -4]));

//document.getElementById("target").innerHTML = a(7);
