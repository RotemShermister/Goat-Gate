# Proposal

## What will (likely) be the title of your project?

GOAT-GATE

## In just a sentence or two, summarize your project. (E.g., "A website that lets you buy and sell stocks.")

A device that alerts when the goat gate opens.

## In a paragraph or more, detail your project. What will your software do? What features will it have? How will it be executed?

For this final project, I will create a notification system that alerts us when the goat gate is open (my boyfriend's family have goats). I will do so by using a raspberry pi and a magnetic switch which is connected via gpio pins. The raspberry pi will be powered by an external source outside and in an enclosure. It will be connected to the house's Wi-Fi network so that it is able to send emails. It will send emails by using the Google API and internal Linux packages. When the switch connection opens (when the gate is opened), an email will be sent to notify that the goat gate has opened. This doubles as a security measure and a way to monitor goat activity!

## If planning to combine 1051's final project with another course's final project, with which other course? And which aspect(s) of your proposed project would relate to 1051, and which aspect(s) would relate to the other course?

N/A

## If planning to collaborate with 1 or 2 classmates for the final project, list their names, email addresses, and the names of their assigned TAs below.

N/A

## In the world of software, most everything takes longer to implement than you expect. And so it's not uncommon to accomplish less in a fixed amount of time than you hope.

### In a sentence (or list of features), define a GOOD outcome for your final project. I.e., what WILL you accomplish no matter what?

I hope that I will be able to setup the raspberry pi and connect it to the magnetic switch (I have never done that before). I think that at minimum, I should be able to configure the raspberry pi and write a program which detects changes in the switch state. 

### In a sentence (or list of features), define a BETTER outcome for your final project. I.e., what do you THINK you can accomplish before the final project's deadline?

A better outcome includes implementation of email sending functionality and network connection from the backyard. I will need to figure out how to connect the raspberry pi to a personal email and send out messages. Additionally, I will need to figure out a way to ensure the raspberry pi has a stable wifi connection from outside (may need to buy a wifi extender).

### In a sentence (or list of features), define a BEST outcome for your final project. I.e., what do you HOPE to accomplish before the final project's deadline?

As previously mentioned, I would like to have switch functionality, power supply, wifi access, and email sending. I would like to be able to send an image over email and more specific information like the time that the goat's got out and if the gate was opened or closed. Potentially I would like to find a more permanent way to implement the system so that it can remain outside.

## In a paragraph or more, outline your next steps. What new skills will you need to acquire? What topics will you need to research? If working with one of two classmates, who will do what?

- Acquire raspberry pi (DONE)
- Order magnetic switch compatible with the raspberry pi (DONE)
- Research how to setup the raspberry pi for Linux
- Install Linux packages and initialize the system
- Learn how to interface with GPIO pins
