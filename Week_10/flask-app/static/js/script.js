// sanity check
// console.log('Everything is linked and workings!');

var button = document.getElementsByClassName('button')[0];

button.addEventListener('mouseover', function(){
  console.log('hello from mr.button');
  button.style.background = 'blue';
});

button.addEventListener('mouseout', function(){
  console.log('BYEE');
  button.style.background = 'red';
});
