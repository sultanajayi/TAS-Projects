// Sort an array of strings in alph. order

function sortArray(array) {
    let newArr = []

    for (let index = 0; index < array.length; index++) {
        newArr.push(array[index].toLowerCase());
        
    }
    return newArr.sort()
}


console.log(sortArray(["Sola","Amoke","Tolani","Chinonso","Ibrahim","Marian"]));