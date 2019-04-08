const Gpio = require("onoff").Gpio; //include onoff to interact with the GPIO
const shell = require("shelljs"); //allows bash script to fire

let message = "sending push notification originating in RPI";

const input = new Gpio(17, "in", "both"); //use GPIO pin 17 as input, and 'both' button presses, and releases should be handled

input.watch(function(err, value) {
  //Watch for hardware interrupts on pushButton GPIO, specify callback function
  if (err) {
    //if an error
    console.error("There was an error", err); //output error message to console
    return;
  }
  console.log("incoming signal detected");

  shell.exec(
    `curl -d '{"message":"${message}"}' -H "Content-Type: application/json" -X POST https://pidoorbellserver.herokuapp.com/message`
  );
});
