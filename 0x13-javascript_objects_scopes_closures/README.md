# JavaScript Classes:

- Class Declaration:

class ClassName {
  constructor() {
    // Constructor code
  }
  
  method1() {
    // Method 1 code
  }
  
  method2() {
    // Method 2 code
  }
  
  // ...more methods
}


- Constructor:

class ClassName {
  constructor(param1, param2) {
    this.param1 = param1;
    this.param2 = param2;
  }
}


- Inheritance:

class ChildClass extends ParentClass {
  constructor() {
    super(); // Call parent constructor
  }
  
  // Additional methods
}



# JavaScript Functions:

- Function Declaration:

function functionName(param1, param2) {
  // Function code
  return result; // Optional return statement
}


- Function Expression:

const functionName = function(param1, param2) {
  // Function code
  return result; // Optional return statement
};


- Arrow Function (ES6):

const functionName = (param1, param2) => {
  // Function code
  return result; // Optional return statement
};


- Default Parameters:

function functionName(param1 = defaultValue1, param2 = defaultValue2) {
  // Function code
}


- Rest Parameters:

function functionName(...params) {
  // params is an array containing all arguments
}


- Spread Operator:

const array = [1, 2, 3];
const newArray = [...array]; // Create a copy of array


- Callback Functions:

function doSomething(callback) {
  // Perform some action
  callback(); // Call the callback function
}

doSomething(() => {
  // Callback function code
});


- Higher-Order Functions:

function higherOrderFunction(callback) {
  // Function code
  callback(); // Call the callback function
}

higherOrderFunction(() => {
  // Callback function code
});


- Closures:

function outerFunction() {
  const outerVar = 'I am outer';

  function innerFunction() {
    const innerVar = 'I am inner';
    console.log(outerVar + ' ' + innerVar);
  }

  return innerFunction;
}

const innerFunc = outerFunction();
innerFunc(); // Prints "I am outer I am inner"


- Promises (ES6):

const promise = new Promise((resolve, reject) => {
  // Perform async operation
  if (success) {
    resolve(result);
  } else {
    reject(error);
  }
});

promise
  .then(result => {
    // Handle success
  })
  .catch(error => {
    // Handle error
  });


- Async/Await (ES8):

async function fetchData() {
  try {
    const response = await fetch(url);
    const data = await response.json();
    return data;
  } catch (error) {
    // Handle error
  }
}
