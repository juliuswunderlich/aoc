const fs = require('fs')
      ,filename = 'input.txt'

//read the text file
fs.readFile(filename, 'utf8', (err, data) => {
  if (err) throw err
  testNumbers(data)
})

function testNumbers(data) {
  let i,j = 0
  for (i = 0; i <= 99; ++i) {
    for (j = 0; j <= 99; ++j) {
      let val = computeProgram(data, i, j)
      console.log(val)
      if (val == 19690720) {
        console.log('The numbers: ', i, j)
        break
      }
    }
  }

}

function computeProgram(data, num1, num2) {
  const original = data.split(',').map(x => +x)
  let mem = original
  const goal = 19690720

  mem[1] = num1
  mem[2] = num2
  for (let i = 0; i < mem.length; i += 4) {
    if (mem[i] == 1)
      mem[mem[i+3]] = mem[mem[i+1]] + mem[mem[i+2]]
    else if (mem[i] == 2)
      mem[mem[i+3]] = mem[mem[i+1]] * mem[mem[i+2]]
    else if(mem[i] == 99)
      break
    else {
      console.log('Something went wrong...')
      break
    }
  }
  return mem[0]
}




