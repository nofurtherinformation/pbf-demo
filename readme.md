# Demo and intro to Pbf

For a decent intro, see [this video](https://youtu.be/46O73On0gyI). To get the Protocol Buffer Schema to language compiler, grab the latest release on [Github](https://github.com/protocolbuffers/protobuf/releases) for your OS. Add it to your env path, or just use the path to where you downloaded and unzipped the executable.

## Compiling Schema to Python
Protoc [flag language] [:output] [input] 
```bash
protoc --python_out :. ./schema/schema.proto
```
This outputs an importable Python script for packing data into your schema.

## Compiling Schema to JS
Using [PBF](https://www.npmjs.com/package/pbf) installed globally
```bash
npm i -g pbf
pbf ./schema/schema.proto > ./schema/jsSchema.js
```

This gives a schema for reading or writing to PBF from JS.

## Packing data from Python
See `py/write_csv_to_pbf.py`

## Reading data from Python
See `py/read_pbf_to_memory.py`

## Reading data from JS
Not totally documented here, but in short:

```js
const Pbf = require('pbf')
const Schemas = require('path-to-compiled-schema')

async function getMyPbf(pbfURL){
    const response = await fetch(pbfURL)
    const repsonseArrayBuffer = await response.arrayBuffer()
    const responsePbf = await new Pbf(responseArrayBuffer)
    const pbfData = await Schemas.Rows.read(pbf)
    // (and do something with the data!)
}
```
