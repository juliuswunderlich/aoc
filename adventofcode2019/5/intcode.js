const fs = require('fs')
      ,filename = 'input.txt'

//read the text file
fs.readFile(filename, 'utf8', (err, data) => {
  if (err) throw err
  computeProgram(data)
})

/*
  Parameter mode 0: position mode
  Parameter mode 1: immediate mod
  ALL instructions have five digits, if they have less the rest is 0
  1: addition
  2: multiplication
  3: write to
  4: output (console log)
*/

function computeProgram(data) {
  const program = data.split(',').map(x => +x)
  let stringProgram = data.split(',')

  //start by making all instructions five digits
  for (s of stringProgram) {
    //check if s is a negative number
    let i = 0
    if (s.charAt(0) == '-') {
      ++i
    }
    } if(s.length - i == 4) {

    } else if(s.length - i == 3) {

    } else if(s.length - i == 2) {

    } else if(s.length - i == 1) {

    }

  }


}

  /*
  for (let i = 0; i < mem.length; i += 4) {
    if (mem[i] == 1)
      mem[mem[i+3]] = mem[mem[i+1]] + mem[mem[i+2]]
    else if (mem[i] == 2)
      mem[mem[i+3]] = mem[mem[i+1]] * mem[mem[i+2]]
    else if (mem[i] == 3)

    else if(mem[i] == 99)
      break
    else {
      console.log('Something went wrong...')
      break
    }
  }
  return mem[0]
  */




