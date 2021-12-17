function isPrime(num) {
  let ans = 0;
  for (let i = 2; i < num; i++) {
    if (num % i == 0) {
      return ans;
    }
  }
  return 1;
}

function findPrimes(limitBottom, limitTop) {
  primes = [];
  for (i = limitBottom; i <= limitTop; i++) {
    if (isPrime(i) == 1) {
      primes.push(i);
    }
  }
  console.log(primes);
}

findPrimes(100000, 1000000);
