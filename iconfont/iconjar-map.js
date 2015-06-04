// load desired modules
var fileSystem = require( 'fs' );
var readLine = require( 'readline' );
var path = require( 'path' );

// file name we want to generate
var MAP_FILE_NAME = 'MaterialIcons-Regular.ijmap';

// create a file streaming interface
var readLineHandle = readLine.createInterface({
  input: fileSystem.createReadStream('codepoints'),
  output: process.stdout,
  terminal: false
});

// read each line by line from the file codepoints file
var json = {icons: {}};
readLineHandle.on('line', function (line) {

  // match the name, space then any unicode after it
  var match = line.split(' ');

  // convert the name into something a little more friendly for IconJar
  // tags will also be based on this
  var unicode = match[1];
  var name = match[0].toLowerCase().replace(/[^0-9a-z]+/gi, ' ').replace(/\b[a-z]/g, function (char) {
    return char.toUpperCase();
  } ).trim();

  // assign the unicode to the name for IconJar
  json.icons[unicode] = {
    name: name
  }
});

readLineHandle.on('close', function () {
  // once reading has finished
  // here we can write the file
  fileSystem.writeFileSync(MAP_FILE_NAME, JSON.stringify(json));
});