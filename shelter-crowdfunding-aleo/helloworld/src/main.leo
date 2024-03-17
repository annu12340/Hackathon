// The 'helloworld' program.
program helloworld.aleo {
    mapping account: address => u64;
  
    record token {
        // The token owner.
        owner: address,
        // The token amount.
        amount: u64,
    }

    transition transfer_public(public receiver: address, public amount: u64) {
        // Transfer the tokens publicly, by invoking the computation on-chain.
        return then finalize(self.caller, receiver, amount);
    }
    finalize transfer_public(public sender: address, public receiver: address, public amount: u64) {
        // Decrements `account[sender]` by `amount`.
        // If `account[sender]` does not exist, it will be created.
        // If `account[sender] - amount` underflows, `transfer_public` is reverted.
        let sender_amount: u64 = Mapping::get_or_use(account, sender, 0u64);
        Mapping::set(account, sender, sender_amount - amount);
        
        // Increments `account[receiver]` by `amount`.
        // If `account[receiver]` does not exist, it will be created.
        // If `account[receiver] + amount` overflows, `transfer_public` is reverted.
        let receiver_amount: u64 = Mapping::get_or_use(account, receiver, 0u64);
        Mapping::set(account, receiver, receiver_amount + amount);
    }


    transition transfer_private_to_public(sender: token, public receiver: address, public amount: u64) -> token {
        // Checks the given token record has a sufficient token amount.
        // This `sub` operation is safe, and the proof will fail if an underflow occurs.
        // `difference` holds the change amount for the caller.
        let difference: u64 = sender.amount - amount;

        // Produces a token record with the change amount for the caller.
        let remaining: token = token {
            owner: sender.owner,
            amount: difference,
        };

        // Output the sender's change record.
        // Increment the token amount publicly for the token receiver.
        return remaining then finalize(receiver, amount);
    }

    finalize transfer_private_to_public(public receiver: address, public amount: u64) {
        // Increments `account[receiver]` by `amount`.
        // If `account[receiver]` does not exist, it will be created.
        // If `account[receiver] + amount` overflows, `transfer_private_to_public` is reverted.
        let receiver_amount: u64 = Mapping::get_or_use(account, receiver, 0u64);
        Mapping::set(account, receiver, receiver_amount + amount);
    }

    transition transfer(token: token, to: address, amount: u64) -> (token, token) {

        // Checks the given token record has sufficient balance.
        // This `sub` operation is safe, and the proof will fail
        // if an overflow occurs.
        // `difference` holds the change amount to be returned to sender.
        let difference: u64 = token.amount - amount;

        // Produce a token record with the change amount for the sender.
        let remaining: token = token {
            owner: token.owner,
            amount: difference,
        };

        // Produce a token record for the specified receiver.
        let transferred: token = token {
            owner: to,
            amount: amount,
        };

        // Output the sender's change record and the receiver's record.
        return (remaining, transferred);
    }

    transition main(public a: u32, b: u32) -> u32 {
        let c: u32 = a + b;
        return c;
    }
}
