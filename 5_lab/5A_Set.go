package main
 
import (
    "io/ioutil"
    "strconv"
    "strings"
)
 
var size = 100000
 
func hashFunction(key int) int {
    key = (key + size) % size
    if key < 0 {
        key = -key
    }
    return key
}
 
func (self *LinkedList) search(value int) *Member{
    index := self.first
    for index != nil{
        if index.value == value{
            return index
        }else{
            index = index.next
        }
    }
    return index
}
type Member struct {
    value int
    next  *Member
    prev  *Member
}
 
type LinkedList struct{
    first* Member
}
func main() {
    array := make([]LinkedList, size)
    result := make([]string,0)
    get, _ := ioutil.ReadFile("set.in")
    getLines := strings.Split(string(get), "\n")
    for i := 0; i < len(getLines); i++ {
        if getLines[i] != "" {
            getCommand := strings.Split(string(getLines[i]), " ")
            value, _ := strconv.Atoi(getCommand[1][:len(getCommand[1])-1])
            var key = hashFunction(value)
            var position = array[key].search(value)
 
            switch getCommand[0] {
            case "insert":
                newMember := &Member{value : value}
                if position == nil {
                    if array[key].first != nil{
                        array[key].first.prev = newMember
                        newMember.next = array[key].first
                    }
                    array[key].first = newMember
                }
            case "delete":
                if position != nil{
                    if position.next != nil{
                        position.next.prev = position.prev
                    }
                    if position.prev != nil{
                        position.prev.next = position.next
                    }else{
                        array[key].first = position.next
                    }
                }
            case "exists":
                if position != nil {
                    result = append(result, "true")
                } else {
                    result = append(result,"false")
                }
            }
        }
    }
    myResult := []byte(strings.Join(result, "\n"))
    _ = ioutil.WriteFile("set.out", myResult, 0777)
 
}
