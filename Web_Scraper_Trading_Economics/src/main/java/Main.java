/*

 */

import io.vertx.core.Vertx;

import java.io.IOException;

public class Main
{
    public static void main(String args[]) throws IOException
    {
        Vertx vertx = Vertx.vertx();

        vertx.deployVerticle(new Server(), stringAsyncResult -> System.out.println("Server deployment complete"));
    }
}