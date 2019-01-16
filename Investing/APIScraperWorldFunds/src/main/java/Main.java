/*
Copyright Jason ALOYAU was born on November 11th, 1993 in Saint-Louis (France)
Date of creation of this software : March 31st, 2018

E-mail of Jason ALOYAU : jason.aloyau@outlook.fr

This software is a computer program whose purpose is to extract data concerning the world funds published on the website :
https://fr.investing.com/funds/world-funds

The world funds data are represented by :
- Name
- Symbol
- Last
- Variation in pourcentage
- Total volume
- Hours

This software is governed by the CeCILL-B license under French law and
abiding by the rules of distribution of free software.  You can  use,
modify and/ or redistribute the software under the terms of the CeCILL-B
license as circulated by CEA, CNRS and INRIA at the following URL
"http://www.cecill.info".

As a counterpart to the access to the source code and  rights to copy,
modify and redistribute granted by the license, users are provided only
with a limited warranty  and the software's author,  the holder of the
economic rights,  and the successive licensors  have only  limited
liability.

In this respect, the user's attention is drawn to the risks associated
with loading,  using,  modifying and/or developing or reproducing the
software by the user in light of its specific status of free software,
that may mean  that it is complicated to manipulate,  and  that  also
therefore means  that it is reserved for developers  and  experienced
professionals having in-depth computer knowledge. Users are therefore
encouraged to load and test the software's suitability as regards their
requirements in conditions enabling the security of their systems and/or
data to be ensured and,  more generally, to use and operate it in the
same conditions as regards security.

The fact that you are presently reading this means that you have had
knowledge of the CeCILL-B license and that you accept its terms.
 */

import io.vertx.core.AsyncResult;
import io.vertx.core.Handler;
import io.vertx.core.Vertx;

import java.io.IOException;

public class Main
{
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