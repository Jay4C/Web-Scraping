import Views.Window;
import io.vertx.core.AsyncResult;
import io.vertx.core.Handler;
import io.vertx.core.Vertx;

import java.io.IOException;

public class Main {
    /*public static void main(String args[]) throws IOException
    {
        Window window = new Window();
    }*/

    public static void main(String args[]) throws IOException
    {
        Vertx vertx = Vertx.vertx();

        vertx.deployVerticle(new Server(), new Handler<AsyncResult<String>>()
        {
            @Override
            public void handle(AsyncResult<String> stringAsyncResult)
            {
                System.out.println("Server deployment complete");
            }
        });
    }
}