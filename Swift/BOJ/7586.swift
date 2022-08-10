//
//  main.swift
//  Algorithm
//
//  Created by Tabber on 2022/08/09.
//

import Foundation

cal()

func cal() {
    // 횟수 입력받기
    guard let t = Int(readLine() ?? "") else { return }
    var tmp: [[Int]] = []
    
    for _ in 0..<t{
        var inputNumber = readLine()!.split(separator: " ").map { Int(String($0))! }
        tmp.append(inputNumber)
    }
    
    for numA in tmp {
        var cnt = 1
        for numB in tmp {
            if numA[0] < numB[0] && numA[1] < numB[1] {
                cnt += 1
            }
        }
        print(cnt, terminator: " ")
    }
    
}




