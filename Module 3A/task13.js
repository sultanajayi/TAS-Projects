const books = {
    title : 'Managing Oneself',
    description : 'A PDF file',
    numberOfPage : 64,
    author : 'Peter F. Drucker',
    reading : true,
    toggleReadingStatus : function(){
        if(books.reading===true){
            books.reading = true
        }else {
            books.reading = false
        }
    }
}


books.toggleReadingStatus()
console.log(books.reading)