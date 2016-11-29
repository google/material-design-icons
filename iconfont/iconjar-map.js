// load desired modules
var fileSystem = require( 'fs' );
var readLine = require( 'readline' );
var path = require( 'path' );
 
// find the filename we wish to use
var name = null;
var dirListing = fileSystem.readdirSync( __dirname );

for( var i = 0; i < dirListing.length; i++ ) {		
	// look for TTF, we want the name of it so
	// we can replace the extension with ijmap
	var fileFound = dirListing[i]
	if( path.extname(fileFound) === '.ttf' )
	{
		name = path.basename(fileFound).replace( path.extname(fileFound), '' );
		break;
	}
};
 
// create a file streaming interface
var readLineHandle = readLine.createInterface({
	input: fileSystem.createReadStream( 'codepoints' ),
	output: process.stdout,
	terminal: false
});
 
// read each line by line from the file codepoints file
var json = {icons:{}};
readLineHandle.on( 'line', function( line ) {
	
	// match the name, space then any unicode after it
	var match = line.match( /(.*)\s([a-f0-9]+)/i );
	
	// convert the name into something a little more friendly for IconJar
	// tags will also be based on this
	var unicode = match[2];
	var name = match[1].toLowerCase().replace( /[^a-z]+/gi, ' ' ).replace( /\b[a-z]/g, function ( char ) {
		return char.toUpperCase();
	} ).trim();
	
	// assign the unicode to the name for IconJar
	json.icons[unicode] = {
		name: name
	}
});
 
readLineHandle.on( 'close', function() {
	// once reading has finished
	// here we can write the file
	fileSystem.writeFileSync( name + '.ijmap', JSON.stringify(json));
} );