package edu.aav66.Chapter1;

import java.util.Scanner;

public class BinarySearch
{
    public static void main( String[] args )
    {
        long[] array = new long[100000000];

        for ( long i = 1; i <= 100000000; i++ )
        {
            array[(int)i - 1] = ( i * 3 ) / 2;
        }

        Scanner keyboard = new Scanner( System.in );

        System.out.printf( "Enter an item to search for (from 1 to %d): ",
                           array[array.length - 1] );
        long input = keyboard.nextLong();

        keyboard.close();

        double[] binarySearchResult = new double[3]; // Position, Attempts, Time (nanoseconds)
        for ( int i = 0; i < binarySearchResult.length; i++ )
            binarySearchResult[i] = binarySearch( array, input )[i];

        System.out.println( "\nBinary Search:" );
        System.out.printf( "- Position in array of item: %.0f\n"
                               + "- Attempts taken to find item: %.0f\n"
                               + "- Time taken to find item: %.0f nanoseconds\n",
                           binarySearchResult[0], binarySearchResult[1], binarySearchResult[2] );

        double[] linearSearchResult = new double[3]; // Position, Attempts, Time (nanoseconds)
        for ( int i = 0; i < linearSearchResult.length; i++ )
            linearSearchResult[i] = linearSearch( array, input )[i];

        System.out.println( "\nLinear Search:" );
        System.out.printf( "- Position in array of item: %.0f\n"
                               + "- Attempts taken to find item: %.0f\n"
                               + "- Time taken to find item: %.0f nanoseconds\n",
                           linearSearchResult[0], linearSearchResult[1], linearSearchResult[2] );

        if ( binarySearchResult[2] < linearSearchResult[2] )
            System.out.printf(
                "\nBinary Search is faster than Linear Search by a factor of %.2f times.\n",
                ( linearSearchResult[2] / binarySearchResult[2] ) );
        else
            System.out.printf(
                "\nLinear Search is faster than nBinary Search by a factor of %.2f times.\n",
                ( binarySearchResult[2] / linearSearchResult[2] ) );
    }

    public static double[] binarySearch( long[] array, long key )
    {
        long startTime = System.nanoTime();

        int counter = 0;
        long low = 0;
        long high = array.length - 1; // 0 indexing

        while ( low <= high )
        {
            long mid = ( low + high ) / 2;
            long guess = array[(int)mid];

            if ( guess == key )
            {
                long endTime = System.nanoTime();
                double elapsedTime = ( endTime - startTime ); // nanoseconds
                return new double[] { mid, counter, elapsedTime };
            }

            else if ( guess < key )
                low = mid + 1;
            else if ( guess > key )
                high = mid - 1;

            counter++;
        }
        long endTime = System.nanoTime();
        double elapsedTime = ( endTime - startTime ); // nanoseconds
        return new double[] { -1, counter, elapsedTime };
    }

    public static double[] linearSearch( long[] array, long key )
    {
        long startTime = System.nanoTime();
        int counter = 0;

        for ( int i = 0; i < array.length; i++ )
        {
            if ( array[i] == key )
            {
                long endTime = System.nanoTime();
                double elapsedTime = ( endTime - startTime ); // nanoseconds
                return new double[] { i, counter, elapsedTime };
            }
            counter++;
        }

        long endTime = System.nanoTime();
        double elapsedTime = ( endTime - startTime ); // nanoseconds
        return new double[] { -1, counter, elapsedTime };
    }
}
