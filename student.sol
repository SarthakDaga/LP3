// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract StudentData {
    // Structure groups the details of one student.
    struct Student {
        uint256 id;
        string name;
        uint256 marks;
    }

    // Dynamic array stores all students. 'public' also creates students(index) getter.
    Student[] public students;

    // Add a student to the array.
    function addStudent(uint256 id, string memory name, uint256 marks) public {
        students.push(Student(id, name, marks));
    }

    // Explicit getter for a student's details (also required in the practical guide).
    function getStudent(uint256 index) public view returns (uint256, string memory, uint256) {
        Student memory s = students[index];
        return (s.id, s.name, s.marks);
    }

    // Return the number of students stored in the array.
    function totalStudents() public view returns (uint256) {
        return students.length;
    }

    // Runs for calls that do not match any function, or Ether sent with data.
    fallback() external payable {}

    // Runs when plain Ether is sent with empty calldata.
    receive() external payable {}
}
