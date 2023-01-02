//
//  main.swift
//  Test
//
//  Created by Tabber on 2023/01/01.
//

// 2775 - 부녀회장이 될테야
// DP 문제
// 사실 DP 보단 구현문제에 가까웠던 문제라고 생각한다.

// DP 문제 특성상 점화식을 찾으려고 했으나, 반복되는 곳을 찾지 못하였다.
// 그래서 무식하게 처음 인덱스 (0층) 부터 for문 돌면서 타고 올라가는 방식을 택했다..

import Foundation

var t = Int(readLine() ?? "") ?? 0

for _ in 0..<t {
    let xNum = Int(readLine() ?? "") ?? 0
    let yNum = Int(readLine() ?? "") ?? 0
    
    var array: [[Int]] = [[]]
    
    for i in 0...xNum {
        var num = 0
        var tmp = Array<Int>()
        for j in 1...yNum {
            if i == 0 {
                tmp.append(j)
            } else {
                num += array[i-1][j-1]
                tmp.append(num)
            }
        }
        
        if i == 0 {
            array[0] = tmp
        } else {
            array.append(tmp)
        }
    }
    
    print(array[xNum][yNum-1])
}
