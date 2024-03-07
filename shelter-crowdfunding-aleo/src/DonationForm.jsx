// DonationForm.js

import React, { useState } from 'react';
import helloworld_program from "../helloworld/build/main.aleo?raw";
import { AleoWorker } from "./workers/AleoWorker.js";
import { ToastContainer, toast } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';

const aleoWorker = AleoWorker();
const DonationForm = (
	{
		onDonate, goal,
		amountRaised
	}) => {
	const [donationAmount, setDonationAmount] = useState("");
	const [goalReached, setGoalReached] = useState(false);
	const [executing, setExecuting] = useState(false);
	const notify = (notif) => toast(notif);

	async function execute(amount) {
		setExecuting(true);
		const result = await aleoWorker.localProgramExecution(
		  helloworld_program,
		  "transfer",
		  ["{owner: aleo1mkj353kl7egtp6s5umee68k02zhqq2xs8xl3yyjvm6auuh6zjcyqlvfqlp.private, amount: 100000u64.private, _nonce: 0group.public}",
		   "aleo1f9xe4saepp6052dhjaghdc3phdzcnt6c9mp9q3ut3hj80hhlpsqqnqny24",
		   `${amount}u64`],
		);
		setExecuting(false);
	
		//alert(JSON.stringify(result));
		notify(JSON.stringify(result));
	}

	const handleDonate = () => {
		if (donationAmount <= 0) {
			alert('Please enter a valid donation amount.');
		} else {
			onDonate(donationAmount);
			setDonationAmount("");
			//aleo smart contract execution
			const res = execute(donationAmount);
			console.log(res);
		}
	};
	const remainingAmount = goal - amountRaised;
	if (remainingAmount <= 0 && !goalReached) {
		setGoalReached(true);
	}

	return (
		<div className="form-section">
			{goalReached ? (
				<div className="goal-reached">
					<h2>Congratulations! Goal Reached!</h2>
					<p>Thank You for the Support</p>
				</div>
			) : (
				<div>
					<input
						type="number"
						placeholder='Enter Amount here'
						value={donationAmount}
						onChange={
							(e) =>
								setDonationAmount(parseInt(e.target.value, 10))
						} />
					<button onClick={handleDonate}>
						Donate
					</button>
					{amountRaised >= goal && <p>
						Congratulations! Goal achieved.
					</p>
					}
					{amountRaised < goal && (
						<p>Remaining amount needed:
							${remainingAmount}</p>
					)}
				</div>
			)}
		<ToastContainer autoClose={15000} />
		</div>
	);
};

export default DonationForm;
