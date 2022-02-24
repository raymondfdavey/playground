function solution(numbers)
{
    let maximum = numbers[0];
    let minimum = numbers[0];

    for (let i = 0; i < numbers.length; i++)
    {
        if (numbers[i] > maximum)
        {
            maximum = numbers[i];
        }
        if (numbers[i] < minimum)
        {
            minimum = numbers[i];
        }
    }
    if (minimum == maximum)
    {
        return minimum * numbers.length;
    }

    noMax = numbers.filter((num) => num != maximum);
    secondMax = Math.max(...noMax);
    const maxIndex = numbers.indexOf(maximum);
    numbers[maxIndex] = maximum - secondMax;
    return solution(numbers);
}

function solution(numbers)
{
    for (let i = 0; i < numbers.length; i++)
    {
        if (numbers[i] > maximum)
        {
            maximum = numbers[i];
        }
        if (numbers[i] < minimum)
        {
            minimum = numbers[i];
        }
    }
    if (minimum == maximum)
    {
        return minimum * numbers.length;
    }

    noMax = numbers.filter((num) => num != maximum);
    secondMax = Math.max(...noMax);
    const maxIndex = numbers.indexOf(maximum);
    numbers[maxIndex] = maximum - secondMax;
    return solution(numbers);
}

let newFunc = function (var) {
}