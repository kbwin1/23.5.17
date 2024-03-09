SearchBtn=document.querySelector('#search')
Word=document.querySelector('#word')
wordsFound=document.querySelector('#words_found')
scoreHtml=document.querySelector('#score_show')
maxScore=document.querySelector('#max_score')
seconds=document.querySelector('#timer')
listOfWords=new Set()
currentScore=0

class Game{
    
    constructor(time = 60){
        this.SearchBtn=document.querySelector('#search')
        this.word=document.querySelector('#word')
        this.time=time
        this.timeR=setInterval(this.secodsPass.bind(this),1000)
        this.handle=addEventListener('click', this.checkValue)
    }
    
//timer of 60 secs
secodsPass(){
    this.time-=1
    
    if (this.time === 0){
        this.RespondClick()
        clearInterval(this.timeR)
        alert("Time OUT!!!!!")
    }
    seconds.innerHTML=`Seconds:${this.time}`
}
  //check the value of the words if they are correct or not and evaluate the words to dont get duplicates and add handle the score


async checkValue(e){
    let newLi=document.createElement("LI")
    let val=this.Word.value
    let points=val.length
    if (e.target === this.SearchBtn){
        e.preventDefault() 
    let resp = await axios.get(("/check"),{params:{word:val}});
    if( resp.data.result === 'ok' && listOfWords.has(val) === false ){
        listOfWords.add(val)
        currentScore+=points
        scoreHtml.innerHTML=`Score: ${currentScore}`
        newLi.innerHTML=val
        wordsFound.appendChild(newLi) 
    }
    if( resp.data.result === 'not-on-board' ){
        alert("not-on-board")
    }
    if( resp.data.result === 'not-word' ){
        alert("not-word")
    }    
    this.Word.value=''
    }
    
}

//stop user to keep playing after 60 secs and update score and times plays
async RespondClick() {
this.handle=removeEventListener('click',this.checkValue)
let resp = await axios.get(("/score"),{params:{score:currentScore,times:1},})

}
}


