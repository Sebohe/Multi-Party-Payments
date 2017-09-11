pragma solidity ^0.4.15;


contract percentSplit {
    address owner;
    uint16 percent;
    address party;
    
    
    function percentSplit() {
        owner = msg.sender;
        percent = 800;
    }

    function setParty(address _address ) only_by(owner){
        party = _address;
    }
    
    function setOwner(address _address) only_by(owner) {
        owner = _address;
    }
    

    function() payable {
        party.transfer(msg.value * percent / 1000);
        owner.transfer(this.balance);
    }
    
    function kill() only_by(owner) { suicide(owner); }
    
    modifier only_by(address _address) { require(msg.sender == _address);  _;  }
}
