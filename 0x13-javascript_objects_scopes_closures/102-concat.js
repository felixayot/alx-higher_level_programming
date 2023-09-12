#!/usr/bin/node
const fileSystem = require('fs');
const f1 = fileSystem.readFileSync(process.argv[2], 'utf8');
const f2 = fileSystem.readFileSync(process.argv[3], 'utf8');
fileSystem.writeFileSync(process.argv[4], f1 + f2);
