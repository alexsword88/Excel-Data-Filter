/* // This file is required by the index.html file and will */
// be executed in the renderer process for that window.
// All of the Node.js APIs are available in this process.

/* var rpc = require('node-json-rpc');
 
var options = {
  // int port of rpc server, default 5080 for http or 5433 for https 
  port: 7749,
  // string domain name or ip of rpc server, default '127.0.0.1' 
  host: 'tcp://127.0.0.1',
  // string with default path, default '/' 
  path: '/RFC2',
  // boolean false to turn rpc checks off, default true 
  strict: true
};
 
// Create a server object with options 
var rpc_client = new rpc.Client(options);

function method_call(method, params)
{
	rpc_client.call(
	  {"jsonrpc": "2.0", "method":method, "params": params},
	  function (err, res) {
		// Did it all work ? 
		console.log(res);
		console.log(err);
		if (err) { console.log(err); }
		else { console.log(res); }
	  }
	);
} */