#!/usr/bin/node
const args = Number(process.argv)

if ((args.length === 1) || (args.length === 2)) {
  return 0;
} else {
  for (let i = 1; i <= args.length; i++) {
    let max;
    // let maxSecond = max;
    if (max > args[i + 1]) {
      max = args[i + 1]
    } else {
      max = args[i]
    }
    console.log(max)
  }
}
