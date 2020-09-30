// PLAY A SOUNDEFFECT WHEN AN ACTION OCCUR

var ac = document.querySelector(".acon")
if(ac != null){
    var audio = new Audio('static/audio/ac.mp3')
    audio.volume = 0.2
    audio.play() 
}
var fan = document.querySelector(".fanon")
if(fan != null){
    var audio = new Audio('static/audio/fan.mp3')
    audio.volume = 1
    audio.play() 
}
var tv = document.querySelector(".tvon")
if(tv != null){
    var audio = new Audio('static/audio/tv.wav')
    audio.volume = 1
    audio.play() 
}
var washer = document.querySelector(".washeron")
if(washer != null){
    var audio = new Audio('static/audio/washer.wav')
    audio.volume = 1
    audio.play() 
}
var radio = document.querySelector(".radioon")
if(radio != null){
    var audio = new Audio('static/audio/radio.wav')
    audio.volume = 0.3
    audio.play() 
}
var water = document.querySelector(".wateron")
if(water != null){
    var audio = new Audio('static/audio/water.wav')
    audio.volume = 1
    audio.play() 
}
var fridge = document.querySelector(".fridgeOpen")
if(fridge != null){
    var audio = new Audio('static/audio/fridge.wav')
    audio.volume = 0.2
    audio.play() 
}
var pc = document.querySelector(".pcon")
if(pc != null){
    var audio = new Audio('static/audio/pc.wav')
    audio.volume = 1
    audio.play() 
}