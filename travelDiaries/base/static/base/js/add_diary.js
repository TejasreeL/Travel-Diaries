const addDiaryBtn = document.querySelector("#add-diary-btn");
const dialogBox = document.querySelector(".b1");
const dialogBox2 = document.querySelector(".b2");
const overlay = document.querySelector("#overlay");
const nextPage = document.querySelector('#nextPage');
const prevPage = document.querySelector('#prevPage');
const username = document.querySelector("#author-username").innerHTML;


addDiaryBtn.addEventListener('click', function(e){
    openDialog();
    e.preventDefault();
    e.stopPropagation(); 
   
});

document.addEventListener('click', function(e){
    if(dialogBox.classList.contains('active')){
        var isDialog = e.target.closest(".b1");
        if(!isDialog && !dialogBox2.classList.contains('active')){
            closeDialog();
        }
    }
})

var closeDialog = function(){
    dialogBox.classList.remove('active');
    overlay.classList.remove('active');

}

var openDialog = function(){
    dialogBox.classList.add('active');
    overlay.classList.add('active');
}

nextPage.addEventListener('click', function(e){
    console.log(e.target)
    dialogBox2.classList.add('active');
    console.log(e.target)
    dialogBox.classList.remove('active');
    e.preventDefault()
    console.log('hey')
})

prevPage.addEventListener('click', function(e){
    dialogBox2.classList.remove('active');
    dialogBox.classList.add('active');
    e.preventDefault();
    e.stopPropagation();

})

async function postData(url, formData) {
    try {
        const response = await fetch(url, {
            method: 'POST',
            body: formData
        });

        if (!response.ok) {
            throw new Error('Network response was not ok');
        }

        const htmlContent = await response.text();
        console.log(htmlContent);

        document.body.innerHTML = htmlContent;

    } catch (error) {
        console.error('Error:', error);
        alert('Error creating diary');
    }
}


function submitForms() {
    var form1Data = new FormData(document.getElementById('form1'));

    form1Data.append('author1', username);
    form1Data.append('author2', document.getElementById('user2').value);
    form1Data.append('author3', document.getElementById('user3').value);
    form1Data.append('author4', document.getElementById('user4').value);
    console.log(form1Data);
    postData('user-home/add-diary', form1Data);

}