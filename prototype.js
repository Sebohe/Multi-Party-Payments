var Web3 = require('web3');

var web3 = new Web3(new Web3.providers.HttpProvider('http://192.168.1.24:8556'));

fs = require('fs');
var inputABI;


fileABI = '/home/eth-dev/ethereum/Multi-Party-Split/ABI/percentSplit.abi'

fs.readFile(fileABI, 'utf8', function(err, data) {
    if (!err) {
        inputABI = data;
        waitForAsync();
    }
    else{
        console.error(err);
        return;
    }
});

function waitForAsync() {
    if (inputABI != null){
        createContract()
    }
    else setTimeout(waitForAsync,500);
}
    
web3.eth.defaultAccount = '';

var account = '';
var gasPrice = '20000000000000'
//              '20000000000000'
function createContract() {
    var contract = new web3.eth.Contract(JSON.parse(inputABI),
            account,
            gasPrice);
    console.log(contract.options.address);
}


