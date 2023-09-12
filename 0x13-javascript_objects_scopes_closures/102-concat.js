#!/usr/bin/node
const fileSource = require('fileSource');
const f1 = fileSource.readFileSync(process.argv[2], 'utf8');
const f2 = fileSource.readFileSync(process.argv[3], 'utf8');
fileSource.writeFileSync(process.argv[4], f1 + f2);
