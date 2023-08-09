class Solution {
    var zeroCount = 0
    var transformCount = 0

    fun solution(s: String): IntArray {
        var input = s
        while (input.length != 1) {
            transformCount++
            input = removeZero(input)
            input = transformBinary(input.length)
        }

        return intArrayOf(transformCount, zeroCount)
    }

    private fun removeZero(s: String): String {
        val transformedString = s.replace("0", "")
        zeroCount += s.length - transformedString.length
        return transformedString
    }

    private fun transformBinary(n: Int): String {
        var tempN = n
        var binaryN = ""
        while (tempN > 0) {
            binaryN += if (tempN % 2 == 0) "0" else "1"
            tempN /= 2
        }
        return binaryN.reversed()
    }
}