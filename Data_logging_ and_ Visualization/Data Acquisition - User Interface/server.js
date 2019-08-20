// Import net module.
var net = require('net');
var dataToWrite1;
var dataToWrite2;
var dataToWrite3;
var dataToWrite4;
var dataToWrite5;
var dataToWrite6;
var fs1 = require('fs');
var fs2 = require('fs');
var fs3 = require('fs');
var fs4 = require('fs');
var fs5 = require('fs');
var fs6 = require('fs');
var express = require ('express');
var app = express();
var Tcp = app.listen(3001);
app.use(express.static('public'));
var socket = require('socket.io');
var io = socket(Tcp);

var Filename;
var Endmsg;
var wstream1 = fs1.createWriteStream('_PPL.txt');
var wstream2 = fs2.createWriteStream('_LT.txt');
var wstream3 = fs3.createWriteStream('_PPL.txt');
var wstream4 = fs4.createWriteStream('_LT.txt');
var wstream5 = fs5.createWriteStream('_PPL.txt');
var wstream6 = fs6.createWriteStream('_LT.txt');

io.sockets.on('connection', newConnection);

function newConnection(socket) {
    console.log('new Connection: '+ socket.id);
    socket.on('record1',recordmessage1);
    socket.on('record2',recordmessage2);
}
//
    function recordmessage1(record_data1) {
         Filename = record_data1.name;
         console.log(Filename);
         if(Filename){
             console.log('name received');
         }
         wstream1 = fs1.createWriteStream(Filename + '_RightThigh.txt');
         wstream2 = fs2.createWriteStream(Filename + '_RightShank.txt');
         wstream3 = fs3.createWriteStream(Filename + '_RightInsole.txt');
         wstream4 = fs4.createWriteStream(Filename + '_LeftThigh.txt');
         wstream5 = fs5.createWriteStream(Filename + '_LeftShank.txt');
         wstream6 = fs6.createWriteStream(Filename + '_LeftInsole.txt');
         Storing(Filename);
     }

    function recordmessage2(record_data2) {
          Endmsg = record_data2.name;
           console.log(Endmsg);
           if(Endmsg){
               console.log('DataAcq Complete');
           }
		setTimeout((function() {  
    		return process.exit(22);
		}), 1000);
      }


function Storing(x) {

    console.log(x);
    ////////////////////////////////////////////////////////////////////////////////
    ////////////////////////_RightThigh ////////////////////////////////////////////
    var option1 = {
        host: "192.168.2.34",
        port: 2330
    }
    // Create TCP client.
    var client1 = net.createConnection(option1, function() {
        //console.log('Connection name : );
        console.log('Connection local address : ' + client1.localAddress + ":" + client1.localPort);
        console.log('Connection remote address : ' + client1.remoteAddress + ":" + client1.remotePort);
    });
    client1.setTimeout(5);
    client1.setEncoding('utf8');
    // When receive server send back data.
    client1.on('data', function(data1) {
        // if (Endmsg) {
        //     //console.log('stop1');
        // }
        // else {
            dataToWrite1 = data1;
            //console.log('Plantar Insole Data : ' + dataToWrite5);
            //wstream1.write('\n');
            wstream1.write(dataToWrite1);
        //}
    });
    // When connection disconnected.
    client1.on('end', function() {
        //console.log('Client socket disconnect. ');
    });
    client1.on('timeout', function() {
        //console.log('Client connection timeout. ');
    });
    client1.on('error', function(err1) {
        //console.error(JSON.stringify(err1));
    });

    ////////////////////////////////////////////////////////////////////////////////
    ////////////////////////_RightShank////////////////////////////////////////////
    var option2 = {
        host: "192.168.2.35",
        port: 2331
    }
    // Create TCP client.
    var client2 = net.createConnection(option2, function() {
        //console.log('Connection name : );
        console.log('Connection local address : ' + client2.localAddress + ":" + client2.localPort);
        console.log('Connection remote address : ' + client2.remoteAddress + ":" + client2.remotePort);
    });
    client2.setTimeout(5);
    client2.setEncoding('utf8');
    // When receive server send back data.
    client2.on('data', function(data2) {
        // if (Endmsg) {
        //     //console.log('stop2');
        // }
        // else {
            dataToWrite2 = data2;
            //console.log('Plantar Insole Data : ' + dataToWrite2);
            //wstream2.write('\n');
            wstream2.write(dataToWrite2);
        //}
    });
    // When connection disconnected.
    client2.on('end', function() {
        //console.log('Client socket disconnect. ');
    });
    client2.on('timeout', function() {
        //console.log('Client connection timeout. ');
    });
    client2.on('error', function(err2) {
        //console.error(JSON.stringify(err2));
    });


    ////////////////////////////////////////////////////////////////////////////////
    ////////////////////////_RightInsole////////////////////////////////////////////
    var option3 = {
        host: "192.168.2.36",
        port: 2332
    }
    // Create TCP client.
    var client3 = net.createConnection(option3, function() {
        //console.log('Connection name : );
        console.log('Connection local address : ' + client3.localAddress + ":" + client3.localPort);
        console.log('Connection remote address : ' + client3.remoteAddress + ":" + client3.remotePort);
    });
    client3.setTimeout(5);
    client3.setEncoding('utf8');
    // When receive server send back data.
    client3.on('data', function(data3) {
        // if (Endmsg) {
        //     //console.log('stop3');
        // }
        // else {
            dataToWrite3 = data3;
            //console.log('Plantar Insole Data : ' + dataToWrite3);
            //wstream3.write('\n');
            wstream3.write(dataToWrite3);
        //}
    });
    // When connection disconnected.
    client3.on('end', function() {
        //console.log('Client socket disconnect. ');
    });
    client3.on('timeout', function() {
        //console.log('Client connection timeout. ');
    });
    client3.on('error', function(err3) {
        //console.error(JSON.stringify(err3));
    });

    ////////////////////////////////////////////////////////////////////////////////
    ////////////////////////_LeftThigh ////////////////////////////////////////////
    var option4 = {
        host: "192.168.2.44",
        port: 3330
    }
    // Create TCP client.
    var client4 = net.createConnection(option4, function() {
        //console.log('Connection name : );
        console.log('Connection local address : ' + client4.localAddress + ":" + client4.localPort);
        console.log('Connection remote address : ' + client4.remoteAddress + ":" + client4.remotePort);
    });
    client4.setTimeout(5);
    client4.setEncoding('utf8');
    // When receive server send back data.
    client4.on('data', function(data4) {
        // if (Endmsg) {
        //     //console.log('stop4');
        // }
        // else {
            dataToWrite4 = data4;
            //console.log('Plantar Insole Data : ' + dataToWrite5);
            //wstream4.write('\n');
            wstream4.write(dataToWrite4);
        // }
    });
    // When connection disconnected.
    client4.on('end', function() {
        //console.log('Client socket disconnect. ');
    });
    client4.on('timeout', function() {
        //console.log('Client connection timeout. ');
    });
    client4.on('error', function(err4) {
        //console.error(JSON.stringify(err4));
    });

    ////////////////////////////////////////////////////////////////////////////////
    ////////////////////////_LeftShank////////////////////////////////////////////
    var option5 = {
        host: "192.168.2.45",
        port: 3331
    }
    // Create TCP client.
    var client5 = net.createConnection(option5, function() {
        //console.log('Connection name : );
        console.log('Connection local address : ' + client5.localAddress + ":" + client5.localPort);
        console.log('Connection remote address : ' + client5.remoteAddress + ":" + client5.remotePort);
    });
    client5.setTimeout(5);
    client5.setEncoding('utf8');
    // When receive server send back data.
    client5.on('data', function(data5) {
        // if (Endmsg) {
        //     //console.log('stop5');
        // }
        // else {
            dataToWrite5 = data5;
            //console.log('Plantar Insole Data : ' + dataToWrite5);
            //wstream5.write('\n');
            wstream5.write(dataToWrite5);
        // }
    });
    // When connection disconnected.
    client5.on('end', function() {
        //console.log('Client socket disconnect. ');
    });
    client5.on('timeout', function() {
        //console.log('Client connection timeout. ');
    });
    client5.on('error', function(err5) {
        //console.error(JSON.stringify(err5));
    });


    ////////////////////////////////////////////////////////////////////////////////
    ////////////////////////_LeftInsole////////////////////////////////////////////
    var option6 = {
        host: "192.168.2.46",
        port: 3332
    }
    // Create TCP client.
    var client6 = net.createConnection(option6, function() {
        //console.log('Connection name : );
        console.log('Connection local address : ' + client6.localAddress + ":" + client6.localPort);
        console.log('Connection remote address : ' + client6.remoteAddress + ":" + client6.remotePort);
    });
    client6.setTimeout(5);
    client6.setEncoding('utf8');
    // When receive server send back data.
    client6.on('data', function(data6) {
        // if (Endmsg) {
        //     //console.log('stop6');
        // }
        // else {
            dataToWrite6 = data6;
            //console.log('Plantar Insole Data : ' + dataToWrite6);
            //wstream6.write('\n');
            wstream6.write(dataToWrite6);
        // }
    });
    // When connection disconnected.
    client6.on('end', function() {
        //console.log('Client socket disconnect. ');
    });
    client6.on('timeout', function() {
        //console.log('Client connection timeout. ');
    });
    client6.on('error', function(err6) {
        //console.error(JSON.stringify(err6));
    });

}
