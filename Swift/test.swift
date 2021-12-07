import Foundation

func solution(_ new_id:String) -> String {
    
    var answer: String = new_id
    let check: [String] = [ "-", "_", "." ]
    // 1단계
    answer = new_id
                .lowercased()
                .replacingOccurrences(of: #"[^\w.-]"#, with: "", options: .regularExpression)
                .replacingOccurrences(of: #"\.{2,}"#, with: ".", options: .regularExpression)
                .trimmingCharacters(in: CharacterSet(charactersIn: "."))
                .checkString { $0.isEmpty ? "a" : $0 }
                .checkString { $0.count >= 16 ? String($0[..<$0.index($0.startIndex, offsetBy: 15)]) : $0}
                .trimmingCharacters(in: CharacterSet(charactersIn: "."))
                .checkString { $0.count <= 2 ? $0.padding(toLength: 3, withPad: String($0.last!), startingAt: 0) : $0 }
    print(answer)
    
    
    return answer
}

extension String {
    func checkString(_ text: (String) -> String) -> String {
        return text(self)
    }
}