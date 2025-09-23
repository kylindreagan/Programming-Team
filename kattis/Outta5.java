import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

//CHANGE TO MAIN FOR UVA JUDGE

public class Outta5 {

    public static boolean backtrack_calculate(List<Integer> nums, Integer total, int curr) {
        if (curr == 5) {
            return total == 23;
        }
        int num = nums.get(curr); 
        return (backtrack_calculate(nums, total+num, curr+1) || backtrack_calculate(nums, total-num, curr+1) || backtrack_calculate(nums, total*num, curr+1));
    }

    public static boolean all_zeros(int[] nums) {
        for (int i=0; i<5; i++) {
            if (nums[i] != 0) {
                    return false;
            }
        }
        return true;
    }

    // https://www.geeksforgeeks.org/print-all-possible-permutations-of-an-array-vector-without-duplicates-using-backtracking/#
    static void permutations(List<List<Integer>> res, 
                                         int[] arr, int idx) {
      
        // Base case: if idx reaches the size of the array,
        // add the permutation to the result
        if (idx == arr.length) {
            res.add(convertArrayToList(arr));
            return;
        }

        // Permutations made by swapping each element
        // starting from index `idx`
        for (int i = idx; i < arr.length; i++) {
            // Swapping
            swap(arr, idx, i);

            // Recursive call to create permutations
            // for the next element
            permutations(res, arr, idx + 1);

            // Backtracking
            swap(arr, idx, i);
        }
    }

    static List<List<Integer>> permute(int[] arr) {
      
        List<List<Integer>> res = new ArrayList<>();
        
        permutations(res, arr, 0);
        return res;
    }

    static void swap(int[] arr, int i, int j) {
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }

    static List<Integer> convertArrayToList(int[] arr) {
        List<Integer> list = new ArrayList<>();
        for (int num : arr) {
            list.add(num);
        }
        return list;
    }
    

    public static void main(String args[]) {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        while (true) {
            int[] nums = new int[5];
            String lines = "";
            try {
                lines = br.readLine();    
            }
            catch (IOException e) {
                System.exit(0);
            }
            String[] strs = lines.trim().split("\\s+");
            for (int i = 0; i < strs.length; i++) {
                nums[i] = Integer.parseInt(strs[i]);
            }
            if (all_zeros(nums)) {
                break;
            }
            List<List<Integer>> perms = permute(nums);
            boolean possible = false;
            for (List<Integer> perm : perms) {
                if (backtrack_calculate(perm, perm.get(0), 1)) {
                    possible = true;
                    break;
                }
            }
            if (possible) {
                System.out.println("Possible");
            }
            else {
                System.out.println("Impossible");
            }
        }
    }
}