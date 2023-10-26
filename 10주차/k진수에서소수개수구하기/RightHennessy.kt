import kotlin.math.sqrt

// 타입 진짜 개팍친다..
class Solution {

    fun solution(n: Int, k: Int): Int {
        val convertedN = convertToK(n, k)
        val decimals = getDecimals(convertedN)

        return decimals.size
    }

    private fun convertToK(n: Int, k: Int): Long {
        if (k == 10) return n.toLong()

        var tmpN: Int = n
        var answer = ""
        while (tmpN >= k) {
            answer = (tmpN % k).toString() + answer
            tmpN /= k
        }
        if (tmpN != 0) {
            answer = tmpN.toString() + answer
        }
        return answer.toLong()
    }

    private fun getDecimals(number: Long): MutableList<Long> {
        val tmp = number.toString().split("0")
        val primes = mutableListOf<Long>()
        for (t in tmp) {
            runCatching {
                t.toLong()
            }.onSuccess {
                if (isPrime(it)) {
                    primes.add(it)
                }
            }
        }
        return primes
    }

    private fun isPrime(i: Long): Boolean {
        if (i <= 1) return false
        for (x: Long in 2.toLong()..sqrt(i.toDouble()).toLong()) {
            if (i.toLong() % x == 0L) return false
        }
        return true
    }
}