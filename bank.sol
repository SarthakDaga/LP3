// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract Bank {
    // Store each customer's balance using their wallet address.
    mapping(address => uint256) private balances;

    // Deposit Ether: enter the amount in Remix's Value field.
    function deposit() public payable {
        require(msg.value > 0, "Send some ether");
        balances[msg.sender] += msg.value;
    }

    // Withdraw an amount in wei from the caller's balance.
    function withdraw(uint256 amount) public {
        require(balances[msg.sender] >= amount, "Insufficient balance");
        balances[msg.sender] -= amount; // Update balance before sending Ether.
        payable(msg.sender).transfer(amount);
    }

    // Show the balance of the caller. The returned value is in wei.
    function showBalance() public view returns (uint256) {
        return balances[msg.sender];
    }
}
