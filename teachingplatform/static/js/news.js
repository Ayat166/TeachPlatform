
function render(){
    const data=JSON.parse(localStorage.getItem('key'))
    document.getElementById('tit').innerHTML = data.title;
    document.getElementById('pho').src=data.urlToImage;
    document.getElementById('des').innerHTML = data.description;
    document.getElementById('con').innerHTML = data.content;

    console.log(data);
}
render();