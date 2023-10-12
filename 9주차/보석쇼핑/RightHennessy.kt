class Solution {
    private val gemSet = mutableSetOf<String>() // gem 종류
    private val gemStore = mutableMapOf<String, Int>() // 현재 가진 각 gem의 최소 index
    private val gemCollect = mutableSetOf<String>() // 현재 모은 gem의 종류
    private var answer = intArrayOf()

    fun solution(gems: Array<String>): IntArray {
        getGemSet(gems)

        for (i in gems.indices) {
            gemStore[gems[i]] = i
            gemCollect.add(gems[i])
            if (gemCollect.size == gemSet.size) {
                addAnswer(i)
            }
        }

        return answer
    }

    private fun getGemSet(gems: Array<String>) {
        for (x in gems) {
            gemSet.add(x)
        }
    }

    private fun addAnswer(max: Int) {
        val min = gemStore.minOf { it.value }
        if (answer.isEmpty()) {
            answer = (intArrayOf(min + 1, max + 1))
            return
        }
        if (answer[1] - answer[0] > max - min) {
            answer = (intArrayOf(min + 1, max + 1))
        }
    }
}