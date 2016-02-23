import java.util.Arrays;
public class GameCard{
   /*
   The board is listed as below:
	        | 0 |
	| 1 | 2 | 3 |
 	    | 4 | 5 | 6 |
 	        | 7 |
   */
   char[] board = {'A', 'A', 'J', 'J', 'K', 'K', 'Q', 'Q'};

   static boolean inArray(char i, char[] a){
      int size = a.length;
      if (size == 0) return false;
      else return (i == a[size-1] || inArray(i,Arrays.copyOfRange(a, 0, size-1)));
   } 

   char[] surround(int i){
      switch (i){
			case 0:
				return new char[]{board[3]};
			case 1:
				return new char[]{board[2]};
			case 2:
				return new char[]{board[1],board[3],board[4]};
			case 3:
				return new char[]{board[0],board[2],board[5]};
			case 4:
				return new char[]{board[2],board[5]};
			case 5:
				return new char[]{board[3],board[4],board[6],board[7]};
//			case 6:
//			case 7:
			default:
				return new char[]{board[5]};
      }
   }

	boolean test(){
		return test(1) && test(2) && test(3) && test(4) && test(5) && test(6)
			&& test(7) && test(0);
	}

	boolean test(int i){
		return test(board[i], surround(i));
	}

	boolean test(char i, char[] a){
		if (i == 'J') return !inArray('J',a);
		else if (i == 'Q') return inArray('J',a) && !inArray('A',a) && !inArray('Q',a);
		else if (i == 'K') return inArray('Q',a) && !inArray('K',a);
		else return inArray('K',a) && !inArray('Q',a) && !inArray('A',a);
	}

	void print(){
		System.out.println("        +---+");
		System.out.println("        | "+board[0]+" |");
		System.out.println("+---+---+---+");
		System.out.println("| "+board[1]+" | "+board[2]+" | "+board[3]+" |");
		System.out.println("+---+---+---+---+");
		System.out.println("    | "+board[4]+" | "+board[5]+" | "+board[6]+" |");
		System.out.println("    +---+---+---+");
		System.out.println("        | "+board[7]+" |");
		System.out.println("        +---+");
		System.out.println();
	}

	public static boolean permuteLexically(char[] data) {
		int k = data.length - 2;
   	while (data[k] >= data[k + 1]) {
			k--;
			if (k < 0) return false;
  		}
		int l = data.length - 1;
		while (data[k] >= data[l]) l--;
		swap(data, k, l);
		int length = data.length - (k + 1);
		for (int i = 0; i < length / 2; i++)
			swap(data, k + 1 + i, data.length - i - 1);
		return true;
	}

	public static void swap(char[] data, int i, int j){
		char temp = data[i];
		data[i] = data[j];
		data[j] = temp;
	}

   public static void main(String[] args){
   	GameCard instance = new GameCard();
		do {
			if (instance.test()) instance.print();
		} while (permuteLexically(instance.board));
	}
}
