class Solution {
  
    public int[] reverse(int[] array) {
        for (int i = 0; i < array.length / 2; i++) {

            int j = array[i];

            array[i] = array[array.length - i - 1];

            array[array.length - i - 1] = j;

        }
        return array;
    }

    public int[][] flipAndInvertImage(int[][] image) {
        int[][] flipimage = new int[image.length][image[0].length];
        for (int i = 0; i < image.length; i++) {
            int[] revarr = reverse(image[i]);
            for (int j = 0; j < revarr.length; j++) {
                flipimage[i][j] = revarr[j] ^= 1;
            }
        }


        return flipimage;
    }
}