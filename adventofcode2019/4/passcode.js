
const NUM1 = 147981;
const NUM2 = 691423;

//check if it contains six digits
const regSix =  new RegExp("[0-9]{6}")
//find pairs of two adjacent digits
const regDubAdj =  new RegExp("(\\d)\\1+")

let counter = 0

for (let i = NUM1; i <= NUM2; ++i) {
  if (checkNumber(i))
    ++counter
}


console.log("Counter: ", counter)
//console.log("Number testet: ", checkNumber(111111))


function checkNumber(num) {
  const sNum = num.toString()
  let arrNum = []

  for (let i = 0, len = sNum.length; i < len; i += 1) {
    arrNum.push(+sNum.charAt(i))
  }

  const resSix = regSix.exec(sNum)
  console.log("Regex Six: ", resSix)
  const resAdj = regDubAdj.exec(sNum)
  console.log("Regex Adj: ", resAdj)
  if (resSix.length != 1 || resAdj < 1 || !checkDecrease(arrNum))
    return false
  return true
}



//check if the numbers are not decreasing
function checkDecrease(arrNum) {
  for (let i = 1; i < arrNum.length; ++i) {
    if (arrNum[i] < arrNum[i-1])
      return false
  }
  return true
}
