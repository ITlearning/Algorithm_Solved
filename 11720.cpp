for(int i = 1; i < text.size(); ++i) {
		if(i - 1 != 0 && i % 10 == 0) {
			cout << text[i] << endl;
		} else {
			cout << text[i];
		}
	}