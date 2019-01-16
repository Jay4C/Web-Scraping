/*

 */

import Model.Wages;
import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.ObjectMapper;
import io.vertx.core.AbstractVerticle;
import io.vertx.core.Future;
import io.vertx.core.http.HttpServer;
import io.vertx.core.http.HttpServerResponse;
import io.vertx.ext.web.Router;
import io.vertx.ext.web.RoutingContext;
import io.vertx.ext.web.handler.BodyHandler;
import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.nodes.Element;
import org.jsoup.select.Elements;

import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

import static Service.ExtractData.ExtractDataModel1;
import static Service.ExtractData.minimumWagesDataset;

public class Server extends AbstractVerticle
{
    //The httpServer starts in this method.
    ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    @Override
    public void start(final Future<Void> startFuture) throws Exception
    {
        HttpServer httpServer = vertx.createHttpServer();

        //Instanciate the router
        final Router router = Router.router(vertx);

        System.out.println("My Server started!");

        router.route().handler(BodyHandler.create());

        //API_Forex_Bot//
        ////////////////////////////////////////////////////////////////////////////////////////////////////////////////

        //Main indicators//
        ////////////////////////////////////////////////////////////////////////////////////////////////////////////////

        //This router permits to use an API to display the GDP growth rate
        //from the URL : https://tradingeconomics.com/country-list/gdp-growth-rate
        router.get("/api/TE/MainIndicators/GdpGrowthRate").handler(this::extractDataMainIndicatorsGdpGrowthRate);

        //This router permits to use an API to display the Interest Rate
        //from the URL : https://tradingeconomics.com/country-list/interest-rate
        router.get("/api/TE/MainIndicators/InterestRate").handler(this::extractDataMainIndicatorsInterestRate);

        //This router permits to use an API to display the Inflation Rate
        //from the URL : https://tradingeconomics.com/country-list/inflation-rate
        router.get("/api/TE/MainIndicators/InflationRate").handler(this::extractDataMainIndicatorsInflationRate);

        //This router permits to use an API to display the Unemployment Rate
        //from the URL : https://tradingeconomics.com/country-list/unemployment-rate
        router.get("/api/TE/MainIndicators/UnemploymentRate").handler(this::extractDataMainIndicatorsUnemploymentRate);

        //This router permits to use an API to display the Government Debt To GDP Rate
        //from the URL : https://tradingeconomics.com/country-list/government-debt-to-gdp
        router.get("/api/TE/MainIndicators/GovernmentDebtToGDPRate").handler(this::extractDataMainIndicatorsGovernmentDebtToGDPRate);

        //This router permits to use an API to display the Balance Of Trade Rate
        //from the URL : https://tradingeconomics.com/country-list/balance-of-trade
        router.get("/api/TE/MainIndicators/BalanceOfTradeRate").handler(this::extractDataMainIndicatorsBalanceOfTradeRate);

        //This router permits to use an API to display the Current Account To GDP Rate
        //from the URL : https://tradingeconomics.com/country-list/current-account-to-gdp
        router.get("/api/TE/MainIndicators/CurrentAccountToGDPRate").handler(this::extractDataMainIndicatorsCurrentAccountToGDPRate);

        ////////////////////////////////////////////////////////////////////////////////////////////////////////////////
        //Main indicators//

        //Markets//
        ////////////////////////////////////////////////////////////////////////////////////////////////////////////////

        //This router permits to use an API to display the Commodity
        //from the URL : https://tradingeconomics.com/commodities
        router.get("/api/TE/Markets/Commodity").handler(this::extractDataMarketsCommodity);

        //This router permits to use an API to display the Currency
        //from the URL : https://tradingeconomics.com/currencies
        router.get("/api/TE/Markets/Currency").handler(this::extractDataMarketsCurrency);

        //This router permits to use an API to display the Government Bond 10 y
        //from the URL : https://tradingeconomics.com/bonds
        router.get("/api/TE/Markets/GovernmentBond10y").handler(this::extractDataMarketsGovernmentBond10y);

        //This router permits to use an API to display the Stock Market
        //from the URL : https://tradingeconomics.com/stocks
        router.get("/api/TE/Markets/StockMarket").handler(this::extractDataMarketsStockMarket);

        ////////////////////////////////////////////////////////////////////////////////////////////////////////////////
        //Markets//

        //Labour//
        ////////////////////////////////////////////////////////////////////////////////////////////////////////////////

        //This router permits to use an API to display the Employed Persons
        //from the URL : https://tradingeconomics.com/country-list/employed-persons
        router.get("/api/TE/Labour/EmployedPersons").handler(this::extractDataLabourEmployedPersons);

        //This router permits to use an API to display the Employment Change
        //from the URL : https://tradingeconomics.com/country-list/employment-change
        router.get("/api/TE/Labour/EmploymentChange").handler(this::extractDataLabourEmploymentChange);

        //This router permits to use an API to display the Employment Rate
        //from the URL : https://tradingeconomics.com/country-list/employment-rate
        router.get("/api/TE/Labour/EmploymentRate").handler(this::extractDataEmploymentRate);

        //This router permits to use an API to display the Full Time Employment
        //from the URL : https://tradingeconomics.com/country-list/full-time-employment
        router.get("/api/TE/Labour/FullTimeEmployment").handler(this::extractDataLabourFullTimeEmployment);

        //This router permits to use an API to display the Initial Jobless Claims
        //from the URL : https://tradingeconomics.com/country-list/initial-jobless-claims
        router.get("/api/TE/Labour/InitialJoblessClaims").handler(this::extractDataLabourInitialJoblessClaims);

        //This router permits to use an API to display the Job Vacancies
        //from the URL : https://tradingeconomics.com/country-list/job-vacancies
        router.get("/api/TE/Labour/JobVacancies").handler(this::extractDataLabourJobVacancies);

        //This router permits to use an API to display the Labor Force Participation Rate
        //from the URL : https://tradingeconomics.com/country-list/labor-force-participation-rate
        router.get("/api/TE/Labour/LaborForceParticipationRate").handler(this::extractDataLabourLaborForceParticipationRate);

        //This router permits to use an API to display the Labour Costs
        //from the URL : https://tradingeconomics.com/country-list/labour-costs
        router.get("/api/TE/Labour/LabourCosts").handler(this::extractDataLabourCosts);

        //This router permits to use an API to display the Long Term Unemployment Rate
        //from the URL : https://tradingeconomics.com/country-list/long-term-unemployment-rate
        router.get("/api/TE/Labour/LongTermUnemploymentRate").handler(this::extractDataLabourNonFarmPayrolls);

        //This router permits to use an API to display the Minimum Wages
        //from the URL : https://tradingeconomics.com/country-list/minimum-wages
        router.get("/api/TE/Labour/MinimumWages").handler(this::scrapeDataMinimumWages);

        //This router permits to use an API to display the Non Farm Payrolls
        //from the URL : https://tradingeconomics.com/country-list/non-farm-payrolls
        router.get("/api/TE/Labour/NonFarmPayrolls").handler(this::extractDataLabourNonFarmPayrolls);

        //This router permits to use an API to display the Part Time Employement
        //from the URL : https://tradingeconomics.com/country-list/part-time-employment
        router.get("/api/TE/Labour/PartTimeEmployement").handler(this::extractDataLabourPartTimeEmployement);

        //This router permits to use an API to display the Population
        //from the URL : https://tradingeconomics.com/country-list/population
        router.get("/api/TE/Labour/Population").handler(this::extractDataLabourPopulation);

        //This router permits to use an API to display the Productivity
        //from the URL : https://tradingeconomics.com/country-list/productivity
        router.get("/api/TE/Labour/Productivity").handler(this::extractDataLabourProductivity);

        //This router permits to use an API to display the RetirementAgeMen
        //from the URL : https://tradingeconomics.com/country-list/retirement-age-men
        router.get("/api/TE/Labour/RetirementAgeMen").handler(this::extractDataLabourRetirementAgeMen);

        //This router permits to use an API to display the RetirementAgeWomen
        //from the URL : https://tradingeconomics.com/country-list/retirement-age-women
        router.get("/api/TE/Labour/RetirementAgeWomen").handler(this::extractDataLabourRetirementAgeWomen);

        //This router permits to use an API to display the Unemployed Persons
        //from the URL : https://tradingeconomics.com/country-list/unemployed-persons
        router.get("/api/TE/Labour/UnemployedPersons").handler(this::extractDataLabourUnemployedPersons);

        //This router permits to use an API to display the Unemployment Rate
        //from the URL : https://tradingeconomics.com/country-list/unemployment-rate
        router.get("/api/TE/Labour/UnemploymentRate").handler(this::extractDataLabourUnemploymentRate);

        //This router permits to use an API to display the Wage Growth
        //from the URL : https://tradingeconomics.com/country-list/wage-growth
        router.get("/api/TE/Labour/WageGrowth").handler(this::extractDataLabourWageGrowth);

        //This router permits to use an API to display the Wages
        //from the URL : https://tradingeconomics.com/country-list/wages
        router.get("/api/TE/Labour/Wages").handler(this::extractDataLabourWages);

        //This router permits to use an API to display the Wages In Manufacturing
        //from the URL : https://tradingeconomics.com/country-list/wages-in-manufacturing
        router.get("/api/TE/Labour/WagesInManufacturing").handler(this::extractDataLabourWagesInManufacturing);

        //This router permits to use an API to display the Youth Unemployment Rate
        //from the URL : https://tradingeconomics.com/country-list/youth-unemployment-rate
        router.get("/api/TE/Labour/YouthUnemploymentRate").handler(this::extractDataLabourYouthUnemploymentRate);

        ////////////////////////////////////////////////////////////////////////////////////////////////////////////////
        //Labour//

        //Prices//
        ////////////////////////////////////////////////////////////////////////////////////////////////////////////////

        //This router permits to use an API to display the Consumer Price Index Cpi
        //from the URL : https://tradingeconomics.com/country-list/consumer-price-index-cpi
        router.get("/api/TE/Prices/ConsumerPriceIndexCpi").handler(this::extractDataPricesConsumerPriceIndexCpi);

        //This router permits to use an API to display the Core Consumer Prices
        //from the URL : https://tradingeconomics.com/country-list/core-consumer-prices
        router.get("/api/TE/Prices/CoreConsumerPrices").handler(this::extractDataPricesCoreConsumerPrices);

        //This router permits to use an API to display the Core Inflation Rate
        //from the URL : https://tradingeconomics.com/country-list/core-inflation-rate
        router.get("/api/TE/Prices/CoreInflationRate").handler(this::extractDataPricesCoreInflationRate);

        //This router permits to use an API to display the Export Prices
        //from the URL : https://tradingeconomics.com/country-list/export-prices
        router.get("/api/TE/Prices/ExportPrices").handler(this::extractDataPricesExportPrices);

        //This router permits to use an API to display the Food Inflation
        //from the URL : https://tradingeconomics.com/country-list/food-inflation
        router.get("/api/TE/Prices/FoodInflation").handler(this::extractDataPricesFoodInflation);

        //This router permits to use an API to display the Gdp Deflator
        //from the URL : https://tradingeconomics.com/country-list/gdp-deflator
        router.get("/api/TE/Prices/GdpDeflator").handler(this::extractDataPricesGdpDeflator);

        //This router permits to use an API to display the Harmonised Consumer Prices
        //from the URL : https://tradingeconomics.com/country-list/harmonised-consumer-prices
        router.get("/api/TE/Prices/HarmonisedConsumerPrices").handler(this::extractDataPricesHarmonisedConsumerPrices);

        //This router permits to use an API to display the Import Prices
        //from the URL : https://tradingeconomics.com/country-list/import-prices
        router.get("/api/TE/Prices/ImportPrices").handler(this::extractDataPricesImportPrices);

        //This router permits to use an API to display the Inflation Rate
        //from the URL : https://tradingeconomics.com/country-list/inflation-rate
        router.get("/api/TE/Prices/InflationRate").handler(this::extractDataPricesInflationRate);

        //This router permits to use an API to display the Inflation Rate Mom
        //from the URL : https://tradingeconomics.com/country-list/inflation-rate-mom
        router.get("/api/TE/Prices/InflationRateMom").handler(this::extractDataPricesInflationRateMom);

        //This router permits to use an API to display the Producer Prices
        //from the URL : https://tradingeconomics.com/country-list/producer-prices
        router.get("/api/TE/Prices/ProducerPrices").handler(this::extractDataPricesProducerPrices);

        //This router permits to use an API to display the Producer Prices Change
        //from the URL : https://tradingeconomics.com/country-list/producer-prices-change
        router.get("/api/TE/Prices/ProducerPricesChange").handler(this::extractDataPricesProducerPricesChange);

        ////////////////////////////////////////////////////////////////////////////////////////////////////////////////
        //Prices//

        //Money//
        ////////////////////////////////////////////////////////////////////////////////////////////////////////////////

        //This router permits to use an API to display the Cash Reserve Ratio
        //from the URL : https://tradingeconomics.com/country-list/cash-reserve-ratio
        router.get("/api/TE/Money/CashReserveRatio").handler(this::extractDataMoneyCashReserveRatio);

        //This router permits to use an API to display the Central Bank Balance Sheet
        //from the URL : https://tradingeconomics.com/country-list/central-bank-balance-sheet
        router.get("/api/TE/Money/CentralBankBalanceSheet").handler(this::extractDataMoneyCentralBankBalanceSheet);

        //This router permits to use an API to display the Deposit Interest Rate
        //from the URL : https://tradingeconomics.com/country-list/deposit-interest-rate
        router.get("/api/TE/Money/DepositInterestRate").handler(this::extractDataMoneyDepositInterestRate);

        //This router permits to use an API to display the Foreign Exchange Reserves
        //from the URL : https://tradingeconomics.com/country-list/foreign-exchange-reserves
        router.get("/api/TE/Money/ForeignExchangeReserves").handler(this::extractDataMoneyForeignExchangeReserves);

        //This router permits to use an API to display the Interbank Rate
        //from the URL : https://tradingeconomics.com/country-list/interbank-rate
        router.get("/api/TE/Money/InterbankRate").handler(this::extractDataMoneyInterbankRate);

        //This router permits to use an API to display the Interest Rate
        //from the URL : https://tradingeconomics.com/country-list/interest-rate
        router.get("/api/TE/Money/InterestRate").handler(this::extractDataMoneyInterestRate);

        //This router permits to use an API to display the Lending Rate
        //from the URL : https://tradingeconomics.com/country-list/lending-rate
        router.get("/api/TE/Money/LendingRate").handler(this::extractDataMoneyLendingRate);

        //This router permits to use an API to display the Loan Growth
        //from the URL : https://tradingeconomics.com/country-list/loan-growth
        router.get("/api/TE/Money/LoanGrowth").handler(this::extractDataMoneyLoanGrowth);

        //This router permits to use an API to display the Loans To Private Sector
        //from the URL : https://tradingeconomics.com/country-list/loans-to-private-sector
        router.get("/api/TE/Money/LoansToPrivateSector").handler(this::extractDataMoneyLoansToPrivateSector);

        //This router permits to use an API to display the Money Supply M0
        //from the URL : https://tradingeconomics.com/country-list/money-supply-m0
        router.get("/api/TE/Money/MoneySupplyM0").handler(this::extractDataMoneyMoneySupplyM0);

        //This router permits to use an API to display the Money Supply M1
        //from the URL : https://tradingeconomics.com/country-list/money-supply-m1
        router.get("/api/TE/Money/MoneySupplyM1").handler(this::extractDataMoneyMoneySupplyM1);

        //This router permits to use an API to display the Money Supply M2
        //from the URL : https://tradingeconomics.com/country-list/money-supply-m2
        router.get("/api/TE/Money/MoneySupplyM2").handler(this::extractDataMoneyMoneySupplyM2);

        //This router permits to use an API to display the Money Supply M3
        //from the URL : https://tradingeconomics.com/country-list/money-supply-m3
        router.get("/api/TE/Money/MoneySupplyM3").handler(this::extractDataMoneyMoneySupplyM3);

        //This router permits to use an API to display the Banks Balance Sheet
        //from the URL : https://tradingeconomics.com/country-list/banks-balance-sheet
        router.get("/api/TE/Money/BanksBalanceSheet").handler(this::extractDataMoneyBanksBalanceSheet);

        ////////////////////////////////////////////////////////////////////////////////////////////////////////////////
        //Money//

        //Trade//
        ////////////////////////////////////////////////////////////////////////////////////////////////////////////////

        //This router permits to use an API to display the Balance Of Trade
        //from the URL : https://tradingeconomics.com/country-list/balance-of-trade
        router.get("/api/TE/Trade/BalanceOfTrade").handler(this::extractDataTradeBalanceOfTrade);

        //This router permits to use an API to display the Capital Flows
        //from the URL : https://tradingeconomics.com/country-list/capital-flows
        router.get("/api/TE/Trade/CapitalFlows").handler(this::extractDataTradeCapitalFlows);

        //This router permits to use an API to display the Crude Oil Production
        //from the URL : https://tradingeconomics.com/country-list/crude-oil-production
        router.get("/api/TE/Trade/CrudeOilProduction").handler(this::extractDataTradeCrudeOilProduction);

        //This router permits to use an API to display the Current Account
        //from the URL : https://tradingeconomics.com/country-list/current-account
        router.get("/api/TE/Trade/CurrentAccount").handler(this::extractDataTradeCurrentAccount);

        //This router permits to use an API to display the Current Account To Gdp
        //from the URL : https://tradingeconomics.com/country-list/current-account-to-gdp
        router.get("/api/TE/Trade/CurrentAccountToGdp").handler(this::extractDataTradeCurrentAccountToGdp);

        //This router permits to use an API to display the Exports
        //from the URL : https://tradingeconomics.com/country-list/exports
        router.get("/api/TE/Trade/Exports").handler(this::extractDataTradeExports);

        //This router permits to use an API to display the External Debt
        //from the URL : https://tradingeconomics.com/country-list/external-debt
        router.get("/api/TE/Trade/ExternalDebt").handler(this::extractDataTradeExternalDebt);

        //This router permits to use an API to display the Foreign Direct Investment
        //from the URL : https://tradingeconomics.com/country-list/foreign-direct-investment
        router.get("/api/TE/Trade/ForeignDirectInvestment").handler(this::extractDataTradeForeignDirectInvestment);

        //This router permits to use an API to display the Gold Reserves
        //from the URL : https://tradingeconomics.com/country-list/gold-reserves
        router.get("/api/TE/Trade/GoldReserves").handler(this::extractDataTradeGoldReserves);

        //This router permits to use an API to display the Imports
        //from the URL : https://tradingeconomics.com/country-list/imports
        router.get("/api/TE/Trade/Imports").handler(this::extractDataTradeImports);

        //This router permits to use an API to display the Remittances
        //from the URL : https://tradingeconomics.com/country-list/remittances
        router.get("/api/TE/Trade/Remittances").handler(this::extractDataTradeRemittances);

        //This router permits to use an API to display the Terms Of Trade
        //from the URL : https://tradingeconomics.com/country-list/terms-of-trade
        router.get("/api/TE/Trade/TermsOfTrade").handler(this::extractDataTradeTermsOfTrade);

        //This router permits to use an API to display the Terrorism Index
        //from the URL : https://tradingeconomics.com/country-list/terrorism-index
        router.get("/api/TE/Trade/TerrorismIndex").handler(this::extractDataTradeTerrorismIndex);

        //This router permits to use an API to display the Tourism Revenues
        //from the URL : https://tradingeconomics.com/country-list/tourism-revenues
        router.get("/api/TE/Trade/TourismRevenues").handler(this::extractDataTradeTourismRevenues);

        //This router permits to use an API to display the Tourist Arrivals
        //from the URL : https://tradingeconomics.com/country-list/tourist-arrivals
        router.get("/api/TE/Trade/TouristArrivals").handler(this::extractDataTradeTouristArrivals);

        ////////////////////////////////////////////////////////////////////////////////////////////////////////////////
        //Trade//

        //GDP//
        ////////////////////////////////////////////////////////////////////////////////////////////////////////////////

        //This router permits to use an API to display the Gdp
        //from the URL : https://tradingeconomics.com/country-list/gdp
        router.get("/api/TE/GDP/Gdp").handler(this::extractDataGDPGdp);

        //This router permits to use an API to display the Gdp Annual Growth Rate
        //from the URL : https://tradingeconomics.com/country-list/gdp-annual-growth-rate
        router.get("/api/TE/GDP/GdpAnnualGrowthRate").handler(this::extractDataGDPGdpAnnualGrowthRate);

        //This router permits to use an API to display the Gdp Constant Prices
        //from the URL : https://tradingeconomics.com/country-list/gdp-constant-prices
        router.get("/api/TE/GDP/GdpConstantPrices").handler(this::extractDataGDPGdpConstantPrices);

        //This router permits to use an API to display the Gdp From Agriculture
        //from the URL : https://tradingeconomics.com/country-list/gdp-from-agriculture
        router.get("/api/TE/GDP/GdpFromAgriculture").handler(this::extractDataGDPGdpFromAgriculture);

        //This router permits to use an API to display the Gdp From Construction
        //from the URL : https://tradingeconomics.com/country-list/gdp-from-construction
        router.get("/api/TE/GDP/GdpFromConstruction").handler(this::extractDataGDPGdpFromConstruction);

        //This router permits to use an API to display the Gdp From Manufacturing
        //from the URL : https://tradingeconomics.com/country-list/gdp-from-manufacturing
        router.get("/api/TE/GDP/GdpFromManufacturing").handler(this::extractDataGDPGdpFromManufacturing);

        //This router permits to use an API to display the Gdp From Mining
        //from the URL : https://tradingeconomics.com/country-list/gdp-from-mining
        router.get("/api/TE/GDP/GdpFromMining").handler(this::extractDataGDPGdpFromMining);

        //This router permits to use an API to display the Gdp From Public Administration
        //from the URL : https://tradingeconomics.com/country-list/gdp-from-public-administration
        router.get("/api/TE/GDP/GdpFromPublicAdministration").handler(this::extractDataGDPGdpFromPublicAdministration);

        //This router permits to use an API to display the Gdp From Services
        //from the URL : https://tradingeconomics.com/country-list/gdp-from-services
        router.get("/api/TE/GDP/GdpFromServices").handler(this::extractDataGDPGdpFromServices);

        //This router permits to use an API to display the Gdp From Transport
        //from the URL : https://tradingeconomics.com/country-list/gdp-from-transport
        router.get("/api/TE/GDP/GdpFromTransport").handler(this::extractDataGDPGdpFromTransport);

        //This router permits to use an API to display the gdp-from-utilities
        //from the URL : https://tradingeconomics.com/country-list/gdp-from-utilities
        router.get("/api/TE/GDP/GdpFromUtilities").handler(this::extractDataGDPGdpFromUtilities);

        //This router permits to use an API to display the Gdp Growth Rate
        //from the URL : https://tradingeconomics.com/country-list/gdp-growth-rate
        router.get("/api/TE/GDP/GdpGrowthRate").handler(this::extractDataGDPGdpGrowthRate);

        //This router permits to use an API to display the gdp-per-capita
        //from the URL : https://tradingeconomics.com/country-list/gdp-per-capita
        router.get("/api/TE/GDP/GdpPerCapita").handler(this::extractDataGDPGdpPerCapita);

        //This router permits to use an API to display the Gdp Per Capita Ppp
        //from the URL : https://tradingeconomics.com/country-list/gdp-per-capita-ppp
        router.get("/api/TE/GDP/GdpPerCapitaPpp").handler(this::extractDataGDPGdpPerCapitaPpp);

        //This router permits to use an API to display the Gross Fixed Capital Formation
        //from the URL : https://tradingeconomics.com/country-list/gross-fixed-capital-formation
        router.get("/api/TE/GDP/GrossFixedCapitalFormation").handler(this::extractDataGDPGrossFixedCapitalFormation);

        //This router permits to use an API to display the Gross National Product
        //from the URL : https://tradingeconomics.com/country-list/gross-national-product
        router.get("/api/TE/GDP/GrossNationalProduct").handler(this::extractDataGDPGrossNationalProduct);

        ////////////////////////////////////////////////////////////////////////////////////////////////////////////////
        //GDP//

        //Government//
        ////////////////////////////////////////////////////////////////////////////////////////////////////////////////

        //This router permits to use an API to display the Asylum Applications
        //from the URL : https://tradingeconomics.com/country-list/asylum-applications
        router.get("/api/TE/Government/AsylumApplications").handler(this::extractDataGovernmentAsylumApplications);

        //This router permits to use an API to display the Rating
        //from the URL : https://tradingeconomics.com/country-list/rating
        router.get("/api/TE/Government/Rating").handler(this::extractDataGovernmentRating);

        //This router permits to use an API to display the Fiscal Expenditure
        //from the URL : https://tradingeconomics.com/country-list/fiscal-expenditure
        router.get("/api/TE/Government/FiscalExpenditure").handler(this::extractDataGovernmentFiscalExpenditure);

        //This router permits to use an API to display the Government Budget
        //from the URL : https://tradingeconomics.com/country-list/government-budget
        router.get("/api/TE/Government/GovernmentBudget").handler(this::extractDataGovernmentGovernmentBudget);

        //This router permits to use an API to display the Government Budget Value
        //from the URL : https://tradingeconomics.com/country-list/government-budget-value
        router.get("/api/TE/Government/GovernmentBudgetValue").handler(this::extractDataGovernmentGovernmentBudgetValue);

        //This router permits to use an API to display the Government Debt
        //from the URL : https://tradingeconomics.com/country-list/government-debt
        router.get("/api/TE/Government/GovernmentDebt").handler(this::extractDataGovernmentGovernmentDebt);

        //This router permits to use an API to display the Government Debt To Gdp
        //from the URL : https://tradingeconomics.com/country-list/government-debt-to-gdp
        router.get("/api/TE/Government/GovernmentDebtToGdp").handler(this::extractDataGovernmentGovernmentDebtToGdp);

        //This router permits to use an API to display the Government Revenues
        //from the URL : https://tradingeconomics.com/country-list/government-revenues
        router.get("/api/TE/Government/GovernmentRevenues").handler(this::extractDataGovernmentGovernmentRevenues);

        //This router permits to use an API to display the Government Spending
        //from the URL : https://tradingeconomics.com/country-list/government-spending
        router.get("/api/TE/Government/GovernmentSpending").handler(this::extractDataGovernmentGovernmentSpending);

        //This router permits to use an API to display the
        //from the URL : https://tradingeconomics.com/country-list/government-spending-to-gdp
        router.get("/api/TE/Government/GovernmentSpendingToGdp").handler(this::extractDataGovernmentGovernmentSpendingToGdp);

        //This router permits to use an API to display the Holidays
        //from the URL : https://tradingeconomics.com/holidays
        router.get("/api/TE/Government/Holidays").handler(this::extractData);

        ////////////////////////////////////////////////////////////////////////////////////////////////////////////////
        //Government//

        //Housing//
        ////////////////////////////////////////////////////////////////////////////////////////////////////////////////

        //This router permits to use an API to display the building-permits
        //from the URL : https://tradingeconomics.com/country-list/building-permits
        router.get("/api/TE/Housing/BuildingPermits").handler(this::extractData);

        //This router permits to use an API to display the Construction Output
        //from the URL : https://tradingeconomics.com/country-list/construction-output
        router.get("/api/TE/Housing/ConstructionOutput").handler(this::extractDataHousingConstructionOutput);

        //This router permits to use an API to display the Home Ownership Rate
        //from the URL : https://tradingeconomics.com/country-list/home-ownership-rate
        router.get("/api/TE/Housing/HomeOwnershipRate").handler(this::extractDataHousingHomeOwnershipRate);

        //This router permits to use an API to display the
        //from the URL : https://tradingeconomics.com/country-list/housing-index
        router.get("/api/TE/Housing/HousingIndex").handler(this::extractDataHousingHousingIndex);

        //This router permits to use an API to display the
        //from the URL : https://tradingeconomics.com/country-list/housing-starts
        router.get("/api/TE/Housing/HousingStarts").handler(this::extractDataHousingHousingStarts);

        ////////////////////////////////////////////////////////////////////////////////////////////////////////////////
        //Housing//

        //Business//
        ////////////////////////////////////////////////////////////////////////////////////////////////////////////////

        //This router permits to use an API to display the
        //from the URL : https://tradingeconomics.com/country-list/bankruptcies
        router.get("/api/TE/Business/Bankruptcies").handler(this::extractData);

        //This router permits to use an API to display the Business Confidence
        //from the URL : https://tradingeconomics.com/country-list/business-confidence
        router.get("/api/TE/Business/BusinessConfidence").handler(this::extractDataBusinessBusinessConfidence);

        //This router permits to use an API to display the Capacity Utilization
        //from the URL : https://tradingeconomics.com/country-list/capacity-utilization
        router.get("/api/TE/Business/CapacityUtilization").handler(this::extractDataBusinessCapacityUtilization);

        //This router permits to use an API to display the Car Production
        //from the URL : https://tradingeconomics.com/country-list/car-production
        router.get("/api/TE/Business/CarProduction").handler(this::extractDataBusinessCarProduction);

        //This router permits to use an API to display the Car Registrations
        //from the URL : https://tradingeconomics.com/country-list/car-registrations
        router.get("/api/TE/Business/CarRegistrations").handler(this::extractDataBusinessCarRegistrations);

        //This router permits to use an API to display the Cement Production
        //from the URL : https://tradingeconomics.com/country-list/cement-production
        router.get("/api/TE/Business/CementProduction").handler(this::extractDataBusinessCementProduction);

        //This router permits to use an API to display the Changes In Inventories
        //from the URL : https://tradingeconomics.com/country-list/changes-in-inventories
        router.get("/api/TE/Business/ChangesInInventories").handler(this::extractDataBusinessChangesInInventories);

        //This router permits to use an API to display the Competitiveness Index
        //from the URL : https://tradingeconomics.com/country-list/competitiveness-index
        router.get("/api/TE/Business/CompetitivenessIndex").handler(this::extractDataBusinessCompetitivenessIndex);

        //This router permits to use an API to display the Competitiveness Rank
        //from the URL : https://tradingeconomics.com/country-list/competitiveness-rank
        router.get("/api/TE/Business/CompetitivenessRank").handler(this::extractDataBusinessCompetitivenessRank);

        //This router permits to use an API to display the Composite Pmi
        //from the URL : https://tradingeconomics.com/country-list/composite-pmi
        router.get("/api/TE/Business/CompositePmi").handler(this::extractDataBusinessCompositePmi);

        //This router permits to use an API to display the Corporate Profits
        //from the URL : https://tradingeconomics.com/country-list/corporate-profits
        router.get("/api/TE/Business/CorporateProfits").handler(this::extractDataBusinessCorporateProfits);

        //This router permits to use an API to display the Corruption Index
        //from the URL : https://tradingeconomics.com/country-list/corruption-index
        router.get("/api/TE/Business/CorruptionIndex").handler(this::extractDataBusinessCorruptionIndex);

        //This router permits to use an API to display the Corruption Rank
        //from the URL : https://tradingeconomics.com/country-list/corruption-rank
        router.get("/api/TE/Business/CorruptionRank").handler(this::extractDataBusinessCorruptionRank);

        //This router permits to use an API to display the Ease Of Doing Business
        //from the URL : https://tradingeconomics.com/country-list/ease-of-doing-business
        router.get("/api/TE/Business/EaseOfDoingBusiness").handler(this::extractDataBusinessEaseOfDoingBusiness);

        //This router permits to use an API to display the Electricity Production
        //from the URL : https://tradingeconomics.com/country-list/electricity-production
        router.get("/api/TE/Business/ElectricityProduction").handler(this::extractDataBusinessElectricityProduction);

        //This router permits to use an API to display the Factory Orders
        //from the URL : https://tradingeconomics.com/country-list/factory-orders
        router.get("/api/TE/Business/FactoryOrders").handler(this::extractDataBusinessFactoryOrders);

        //This router permits to use an API to display the Industrial Production
        //from the URL : https://tradingeconomics.com/country-list/industrial-production
        router.get("/api/TE/Business/IndustrialProduction").handler(this::extractDataBusinessIndustrialProduction);

        //This router permits to use an API to display the Industrial Production Mom
        //from the URL : https://tradingeconomics.com/country-list/industrial-production-mom
        router.get("/api/TE/Business/IndustrialProductionMom").handler(this::extractDataBusinessIndustrialProductionMom);

        //This router permits to use an API to display the Internet Speed
        //from the URL : https://tradingeconomics.com/country-list/internet-speed
        router.get("/api/TE/Business/InternetSpeed").handler(this::extractDataBusinessInternetSpeed);

        //This router permits to use an API to display the Ip Addresses
        //from the URL : https://tradingeconomics.com/country-list/ip-addresses
        router.get("/api/TE/Business/IpAddresses").handler(this::extractDataBusinessIpAddresses);

        //This router permits to use an API to display the Leading Economic Index
        //from the URL : https://tradingeconomics.com/country-list/leading-economic-index
        router.get("/api/TE/Business/LeadingEconomicIndex").handler(this::extractDataBusinessLeadingEconomicIndex);

        //This router permits to use an API to display the Manufacturing Pmi
        //from the URL : https://tradingeconomics.com/country-list/manufacturing-pmi
        router.get("/api/TE/Business/ManufacturingPmi").handler(this::extractDataBusinessManufacturingPmi);

        //This router permits to use an API to display the Manufacturing Production
        //from the URL : https://tradingeconomics.com/country-list/manufacturing-production
        router.get("/api/TE/Business/ManufacturingProduction").handler(this::extractDataBusinessManufacturingProduction);

        //This router permits to use an API to display the Mining Production
        //from the URL : https://tradingeconomics.com/country-list/mining-production
        router.get("/api/TE/Business/MiningProduction").handler(this::extractDataBusinessMiningProduction);

        //This router permits to use an API to display the New Orders
        //from the URL : https://tradingeconomics.com/country-list/new-orders
        router.get("/api/TE/Business/NewOrders").handler(this::extractDataBusinessNewOrders);

        //This router permits to use an API to display the Services Pmi
        //from the URL : https://tradingeconomics.com/country-list/services-pmi
        router.get("/api/TE/Business/ServicesPmi").handler(this::extractDataBusinessServicesPmi);

        //This router permits to use an API to display the Small Business Sentiment
        //from the URL : https://tradingeconomics.com/country-list/small-business-sentiment
        router.get("/api/TE/Business/SmallBusinessSentiment").handler(this::extractDataBusinessSmallBusinessSentiment);

        //This router permits to use an API to display the Steel Production
        //from the URL : https://tradingeconomics.com/country-list/steel-production
        router.get("/api/TE/Business/SteelProduction").handler(this::extractDataBusinessSteelProduction);

        //This router permits to use an API to display the Total Vehicle Sales
        //from the URL : https://tradingeconomics.com/country-list/total-vehicle-sales
        router.get("/api/TE/Business/TotalVehicleSales").handler(this::extractDataBusinessTotalVehicleSales);

        //This router permits to use an API to display the Zew Economic Sentiment Index
        //from the URL : https://tradingeconomics.com/country-list/zew-economic-sentiment-index
        router.get("/api/TE/Business/ZewEconomicSentimentIndex").handler(this::extractDataBusinessZewEconomicSentimentIndex);

        ////////////////////////////////////////////////////////////////////////////////////////////////////////////////
        //Business//

        //Consumer//
        ////////////////////////////////////////////////////////////////////////////////////////////////////////////////

        //This router permits to use an API to display the Bank Lending Rate
        //from the URL : https://tradingeconomics.com/country-list/bank-lending-rate
        router.get("/api/TE/Consumer/BankLendingRate").handler(this::extractDataConsumerBankLendingRate);

        //This router permits to use an API to display the Consumer Confidence
        //from the URL : https://tradingeconomics.com/country-list/consumer-confidence
        router.get("/api/TE/Consumer/ConsumerConfidence").handler(this::extractDataConsumerConsumerConfidence);

        //This router permits to use an API to display the Consumer Credit
        //from the URL : https://tradingeconomics.com/country-list/consumer-credit
        router.get("/api/TE/Consumer/ConsumerCredit").handler(this::extractDataConsumerConsumerCredit);

        //This router permits to use an API to display the Consumer Spending
        //from the URL : https://tradingeconomics.com/country-list/consumer-spending
        router.get("/api/TE/Consumer/ConsumerSpending").handler(this::extractDataConsumerConsumerSpending);

        //This router permits to use an API to display the Disposable Personal Income
        //from the URL : https://tradingeconomics.com/country-list/disposable-personal-income
        router.get("/api/TE/Consumer/DisposablePersonalIncome").handler(this::extractDataConsumerDisposablePersonalIncome);

        //This router permits to use an API to display the Gasoline Prices
        //from the URL : https://tradingeconomics.com/country-list/gasoline-prices
        router.get("/api/TE/Consumer/GasolinePrices").handler(this::extractDataConsumerGasolinePrices);

        //This router permits to use an API to display the Households Debt To Gdp
        //from the URL : https://tradingeconomics.com/country-list/households-debt-to-gdp
        router.get("/api/TE/Consumer/HouseholdsDebtToGdp").handler(this::extractDataConsumerHouseholdsDebtToGdp);

        //This router permits to use an API to display the Households Debt To Income
        //from the URL : https://tradingeconomics.com/country-list/households-debt-to-income
        router.get("/api/TE/Consumer/HouseholdsDebtToIncome").handler(this::extractDataConsumerHouseholdsDebtToIncome);

        //This router permits to use an API to display the Personal Savings
        //from the URL : https://tradingeconomics.com/country-list/personal-savings
        router.get("/api/TE/Consumer/PersonalSavings").handler(this::extractDataConsumerPersonalSavings);

        //This router permits to use an API to display the Personal Spending
        //from the URL : https://tradingeconomics.com/country-list/personal-spending
        router.get("/api/TE/Consumer/PersonalSpending").handler(this::extractDataConsumerPersonalSpending);

        //This router permits to use an API to display the Private Sector Credit
        //from the URL : https://tradingeconomics.com/country-list/private-sector-credit
        router.get("/api/TE/Consumer/PrivateSectorCredit").handler(this::extractDataConsumerPrivateSectorCredit);

        //This router permits to use an API to display the Retail Sales Mom
        //from the URL : https://tradingeconomics.com/country-list/retail-sales-mom
        router.get("/api/TE/Consumer/RetailSalesMom").handler(this::extractDataConsumerRetailSalesMom);

        //This router permits to use an API to display the Retail Sales Yoy
        //from the URL : https://tradingeconomics.com/country-list/retail-sales-yoy
        router.get("/api/TE/Consumer/RetailSalesYoy").handler(this::extractDataConsumerRetailSalesYoy);

        ////////////////////////////////////////////////////////////////////////////////////////////////////////////////
        //Consumer//

        //Taxes//
        ////////////////////////////////////////////////////////////////////////////////////////////////////////////////

        //This router permits to use an API to display the Corporate Tax Rate
        //from the URL : https://tradingeconomics.com/country-list/corporate-tax-rate
        router.get("/api/TE/Taxes/CorporateTaxRate").handler(this::extractDataTaxesCorporateTaxRate);

        //This router permits to use an API to display the Personal Income Tax Rate
        //from the URL : https://tradingeconomics.com/country-list/personal-income-tax-rate
        router.get("/api/TE/Taxes/PersonalIncomeTaxRate").handler(this::extractDataTaxesPersonalIncomeTaxRate);

        //This router permits to use an API to display the Sales Tax Rate
        //from the URL : https://tradingeconomics.com/country-list/sales-tax-rate
        router.get("/api/TE/Taxes/SalesTaxRate").handler(this::extractDataTaxesSalesTaxRate);

        //This router permits to use an API to display the Social Security Rate
        //from the URL : https://tradingeconomics.com/country-list/social-security-rate
        router.get("/api/TE/Taxes/SocialSecurityRate").handler(this::extractDataTaxesSocialSecurityRate);

        //This router permits to use an API to display the Social Security Rate For Companies
        //from the URL : https://tradingeconomics.com/country-list/social-security-rate-for-companies
        router.get("/api/TE/Taxes/SocialSecurityRateForCompanies").handler(this::extractDataTaxesSocialSecurityRateForCompanies);

        //This router permits to use an API to display the Social Security Rate For Employees
        //from the URL : https://tradingeconomics.com/country-list/social-security-rate-for-employees
        router.get("/api/TE/Taxes/SocialSecurityRateForEmployees").handler(this::extractDataTaxesSocialSecurityRateForEmployees);

        ////////////////////////////////////////////////////////////////////////////////////////////////////////////////
        //Taxes//

        //Climate//
        ////////////////////////////////////////////////////////////////////////////////////////////////////////////////

        //This router permits to use an API to display the
        //from the URL : https://tradingeconomics.com/country-list/precipitation
        router.get("/api/TE/Climate/Precipitation").handler(this::extractDataClimatePrecipitation);

        //This router permits to use an API to display the
        //from the URL : https://tradingeconomics.com/country-list/temperature
        router.get("/api/TE/Climate/Temperature").handler(this::extractDataClimateTemperature);

        ////////////////////////////////////////////////////////////////////////////////////////////////////////////////
        //Climate//

        //UN_Comtrade_Exports_By_Country//
        ////////////////////////////////////////////////////////////////////////////////////////////////////////////////

        //
        //This router permits to use an API to display the
        //from the URL :
        router.get("/api/TE/").handler(this::extractData);

        //This router permits to use an API to display the
        //from the URL :
        router.get("/api/TE/").handler(this::extractData);

        //This router permits to use an API to display the
        //from the URL :
        router.get("/api/TE/").handler(this::extractData);

        //This router permits to use an API to display the
        //from the URL :
        router.get("/api/TE/").handler(this::extractData);

        ////////////////////////////////////////////////////////////////////////////////////////////////////////////////
        //UN_Comtrade_Exports_By_Country//

        //World Bank//
        ////////////////////////////////////////////////////////////////////////////////////////////////////////////////

        //Agriculture//
        ////////////////////////////////////////////////////////////////////////////////////////////////////////////////

        //This router permits to use an API to display the Agricultural area irrigated (ha)
        //from the URL : https://tradingeconomics.com/country-list/agricultural-area-irrigated-ha-wb-data.html
        router.get("/api/TE/WorldBank/Agriculture/AgriculturalAreaIrrigatedHaWb").handler(this::extractDataWorldBankAgricultureAgriculturalAreaIrrigatedHaWb);

        //This router permits to use an API to display the Agricultural irrigated land (% of total agricultural land)
        //from the URL : https://tradingeconomics.com/country-list/agricultural-irrigated-land-percent-of-total-agricultural-land-wb-data.html
        router.get("/api/TE/WorldBank/Agriculture/AgriculturalIrrigatedLandPercentOfTotalAgriculturalLandWb").handler(this::extractDataWorldBankAgricultureAgriculturalIrrigatedLandPercentOfTotalAgriculturalLandWb);

        //This router permits to use an API to display the Agricultural land (hectares)
        //from the URL : https://tradingeconomics.com/country-list/agricultural-land-hectares-wb-data.html
        router.get("/api/TE/WorldBank/Agriculture/AgriculturalLandHectaresWb").handler(this::extractDataWorldBankAgricultureAgriculturalLandHectaresWb);

        //This router permits to use an API to display the Agricultural machinery, tractors
        //from the URL : https://tradingeconomics.com/country-list/agricultural-machinery-tractors-wb-data.html
        router.get("/api/TE/WorldBank/Agriculture/AgriculturalMachineryTractorsWb").handler(this::extractDataWorldBankAgricultureAgriculturalMachineryTractorsWb);

        //This router permits to use an API to display the Agricultural methane emissions (% of total)
        //from the URL : https://tradingeconomics.com/country-list/agricultural-methane-emissions-percent-of-total-wb-data.html
        router.get("/api/TE/WorldBank/Agriculture/AgriculturalMethaneEmissionsPercentOfTotalWb").handler(this::extractDataWorldBankAgricultureAgriculturalMethaneEmissionsPercentOfTotalWb);

        //This router permits to use an API to display the Agricultural nitrous oxide emissions (% of total)
        //from the URL : https://tradingeconomics.com/country-list/agricultural-nitrous-oxide-emissions-percent-of-total-wb-data.html
        router.get("/api/TE/WorldBank/Agriculture/AgriculturalNitrousOxideEmissionsPercentOfTotalWb").handler(this::extractDataWorldBankAgricultureAgriculturalNitrousOxideEmissionsPercentOfTotalWb);

        //This router permits to use an API to display the Agricultural raw materials exports (% of merchandise exports)
        //from the URL : https://tradingeconomics.com/country-list/agricultural-raw-materials-exports-percent-of-merchandise-exports-wb-data.html
        router.get("/api/TE/WorldBank/Agriculture/AgriculturalRawMaterialsExportsPercentOfMerchandiseExportsWb").handler(this::extractDataWorldBankAgricultureAgriculturalRawMaterialsExportsPercentOfMerchandiseExportsWb);

        //This router permits to use an API to display the Agricultural support estimate (% of GDP)
        //from the URL : https://tradingeconomics.com/country-list/agricultural-support-estimate-percent-of-gdp-wb-data.html
        router.get("/api/TE/WorldBank/Agriculture/AgriculturalSupportEstimatePercentOfGdpWb").handler(this::extractDataWorldBankAgricultureAgriculturalSupportEstimatePercentOfGdpWb);

        //This router permits to use an API to display the Agricultural tractors, exports (FAO, current US$)
        //from the URL : https://tradingeconomics.com/country-list/agricultural-tractors-exports-fao-us-dollar-wb-data.html
        router.get("/api/TE/WorldBank/Agriculture/AgriculturalTractorsExportsFaoUsDollarWb").handler(this::extractDataWorldBankAgricultureAgriculturalTractorsExportsFaoUsDollarWb);

        //This router permits to use an API to display the Agricultural tractors, imports (FAO, current US$)
        //from the URL : https://tradingeconomics.com/country-list/agricultural-tractors-imports-fao-us-dollar-wb-data.html
        router.get("/api/TE/WorldBank/Agriculture/AgriculturalTractorsImportsFaoUsDollarWb").handler(this::extractDataWorldBankAgricultureAgriculturalTractorsImportsFaoUsDollarWb);

        //This router permits to use an API to display the Annual freshwater withdrawals, agriculture (% of total freshwater withdrawal)
        //from the URL : https://tradingeconomics.com/country-list/annual-freshwater-withdrawals-agriculture-percent-of-total-freshwater-withdrawal-wb-data.html
        router.get("/api/TE/WorldBank/Agriculture/AnnualFreshwaterWithdrawalsAgriculturePercentOfTotalFreshwaterWithdrawalWb")
                .handler(this::extractDataWorldBankAgricultureAnnualFreshwaterWithdrawalsAgriculturePercentOfTotalFreshwaterWithdrawalWb);

        //This router permits to use an API to display the Arable land (hectares)
        //from the URL : https://tradingeconomics.com/country-list/arable-land-hectares-wb-data.html
        router.get("/api/TE/WorldBank/Agriculture/ArableLandHectaresWb").handler(this::extractDataWorldBankAgricultureArableLandHectaresWb);

        //This router permits to use an API to display the Average tariffs imposed by developed countries on agricultural products from developing countries
        //from the URL : https://tradingeconomics.com/country-list/average-tariffs-imposed-by-developed-countries-on-agricultural-products-from-developing-countries-wb-data.html
        router.get("/api/TE/WorldBank/Agriculture/AverageTariffsImposedByDevelopedCountriesOnAgriculturalProductsFromDevelopingCountriesWb")
                .handler(this::extractDataWorldBankAgricultureAverageTariffsImposedByDevelopedCountriesOnAgriculturalProductsFromDevelopingCountriesWb);

        //This router permits to use an API to display the Cereal production (metric tons)
        //from the URL : https://tradingeconomics.com/country-list/cereal-production-metric-tons-wb-data.html
        router.get("/api/TE/WorldBank/Agriculture/CerealProductionMetricTonsWb").handler(this::extractDataWorldBankAgricultureCerealProductionMetricTonsWb);

        //This router permits to use an API to display the Crop production index (1999-2001 = 100)
        //from the URL : https://tradingeconomics.com/country-list/crop-production-index-1999-2001--100-wb-data.html
        router.get("/api/TE/WorldBank/Agriculture/CropProductionIndex1999_2001_100Wb").handler(this::extractDataWorldBankAgricultureCropProductionIndex1999_2001_100Wb);

        //This router permits to use an API to display the Employees, agriculture, male (% of male employment)
        //from the URL : https://tradingeconomics.com/country-list/employees-agriculture-male-percent-of-male-employment-wb-data.html
        router.get("/api/TE/WorldBank/Agriculture/EmployeesAgricultureMalePercentOfMaleEmploymentWb").handler(this::extractDataWorldBankAgricultureEmployeesAgricultureMalePercentOfMaleEmploymentWb);

        //This router permits to use an API to display the Fertilizer consumption (% of fertilizer production)
        //from the URL : https://tradingeconomics.com/country-list/fertilizer-consumption-percent-of-fertilizer-production-wb-data.html
        router.get("/api/TE/WorldBank/Agriculture/FertilizerConsumptionPercentOfFertilizerProductionWb").handler(this::extractDataWorldBankAgricultureFertilizerConsumptionPercentOfFertilizerProductionWb);

        //This router permits to use an API to display the Food production index (1999-2001 = 100)
        //from the URL : https://tradingeconomics.com/country-list/food-production-index-1999-2001--100-wb-data.html
        router.get("/api/TE/WorldBank/Agriculture/FoodProductionIndex1999_2001_100Wb").handler(this::extractDataWorldBankAgricultureFoodProductionIndex1999_2001_100Wb);

        //This router permits to use an API to display the Forest area (sq. km)
        //from the URL : https://tradingeconomics.com/country-list/forest-area-sq-km-wb-data.html
        router.get("/api/TE/WorldBank/Agriculture/ForestAreaSqKmWb").handler(this::extractDataWorldBankAgricultureForestAreaSqKmWb);

        //This router permits to use an API to display the Land under cereal production (hectares)
        //from the URL : https://tradingeconomics.com/country-list/land-under-cereal-production-hectares-wb-data.html
        router.get("/api/TE/WorldBank/Agriculture/LandUnderCerealProductionHectaresWb").handler(this::extractDataWorldBankAgricultureLandUnderCerealProductionHectaresWb);

        //This router permits to use an API to display the Real agricultural GDP growth rates
        //from the URL : https://tradingeconomics.com/country-list/real-agricultural-gdp-growth-rates-wb-data.html
        router.get("/api/TE/WorldBank/Agriculture/RealAgriculturalGdpGrowthRatesWb").handler(this::extractDataWorldBankAgricultureRealAgriculturalGdpGrowthRatesWb);

        //This router permits to use an API to display the Rural land area (sq. km)
        //from the URL : https://tradingeconomics.com/country-list/rural-land-area-sq-km-wb-data.html
        router.get("/api/TE/WorldBank/Agriculture/RuralLandAreaSqKmWb").handler(this::extractDataWorldBankAgricultureRuralLandAreaSqKmWb);

        //This router permits to use an API to display the Rural land area where elevation is below 5 meters (sq. km)
        //from the URL : https://tradingeconomics.com/country-list/rural-land-area-where-elevation-is-below-5-meters-sq-km-wb-data.html
        router.get("/api/TE/WorldBank/Agriculture/RuralLandAreaWhereElevationIsBelow5MetersSqKmWb").handler(this::extractDataWorldBankAgricultureRuralLandAreaWhereElevationIsBelow5MetersSqKmWb);

        //This router permits to use an API to display the Total agricultural imports (FAO, current US$)
        //from the URL : https://tradingeconomics.com/country-list/total-agricultural-imports-fao-us-dollar-wb-data.html
        router.get("/api/TE/WorldBank/Agriculture/TotalAgriculturalImportsFaoUsDollarWb").handler(this::extractDataWorldBankAgricultureTotalAgriculturalImportsFaoUsDollarWb);

        //This router permits to use an API to display the Agricultural census
        //from the URL : https://tradingeconomics.com/country-list/agricultural-census-wb-data.html
        router.get("/api/TE/WorldBank/Agriculture/AgriculturalCensusWb").handler(this::extractDataWorldBankAgricultureAgriculturalCensusWb);

        //This router permits to use an API to display the Agricultural land (% of land area)
        //from the URL : https://tradingeconomics.com/country-list/agricultural-land-percent-of-land-area-wb-data.html
        router.get("/api/TE/WorldBank/Agriculture/AgriculturalLandPercentOfLandAreaWb").handler(this::extractDataWorldBankAgricultureAgriculturalLandPercentOfLandAreaWb);

        //This router permits to use an API to display the Agricultural land (sq. km)
        //from the URL : https://tradingeconomics.com/country-list/agricultural-land-sq-km-wb-data.html
        router.get("/api/TE/WorldBank/Agriculture/AgriculturalLandSqKmWb").handler(this::extractDataWorldBankAgricultureAgriculturalLandSqKmWb);

        //This router permits to use an API to display the Agricultural machinery, tractors per 100 sq. km of arable land
        //from the URL : https://tradingeconomics.com/country-list/agricultural-machinery-tractors-per-100-sq-km-of-arable-land-wb-data.html
        router.get("/api/TE/WorldBank/Agriculture/AgriculturalMachineryTractorsPer100SqKmOfArableLandWb").handler(this::extractDataWorldBankAgricultureAgriculturalMachineryTractorsPer100SqKmOfArableLandWb);

        //This router permits to use an API to display the Agricultural methane emissions (thousand metric tons of CO2 equivalent)
        //from the URL : https://tradingeconomics.com/country-list/agricultural-methane-emissions-thousand-metric-tons-of-co2-equivalent-wb-data.html
        router.get("/api/TE/WorldBank/Agriculture/AgriculturalMethaneEmissionsThousandMetricTonsOfCo2EquivalentWb")
                .handler(this::extractDataWorldBankAgricultureAgriculturalMethaneEmissionsThousandMetricTonsOfCo2EquivalentWb);

        //This router permits to use an API to display the Agricultural nitrous oxide emissions (thousand metric tons of CO2 equivalent)
        //from the URL : https://tradingeconomics.com/country-list/agricultural-nitrous-oxide-emissions-thousand-metric-tons-of-co2-equivalent-wb-data.html
        router.get("/api/TE/WorldBank/Agriculture/AgriculturalNitrousOxideEmissionsThousandMetricTonsOfCo2EquivalentWb")
                .handler(this::extractDataWorldBankAgricultureAgriculturalNitrousOxideEmissionsThousandMetricTonsOfCo2EquivalentWb);

        //This router permits to use an API to display the Agricultural raw materials imports (% of merchandise imports)
        //from the URL : https://tradingeconomics.com/country-list/agricultural-raw-materials-imports-percent-of-merchandise-imports-wb-data.html
        router.get("/api/TE/WorldBank/Agriculture/AgriculturalRawMaterialsImportsPercentOfMerchandiseImportsWb")
                .handler(this::extractDataWorldBankAgricultureAgriculturalRawMaterialsImportsPercentOfMerchandiseImportsWb);

        //This router permits to use an API to display the Agricultural tractors, exports
        //from the URL : https://tradingeconomics.com/country-list/agricultural-tractors-exports-wb-data.html
        router.get("/api/TE/WorldBank/Agriculture/AgriculturalTractorsExportsWb").handler(this::extractDataWorldBankAgricultureAgriculturalTractorsExportsWb);

        //This router permits to use an API to display the Agricultural tractors, imports
        //from the URL : https://tradingeconomics.com/country-list/agricultural-tractors-imports-wb-data.html
        router.get("/api/TE/WorldBank/Agriculture/AgriculturalTractorsImportsWb").handler(this::extractDataAgriculturalTractorsImportsWb);

        //This router permits to use an API to display the Agriculture value added per worker (constant 2000 US$)
        //from the URL : https://tradingeconomics.com/country-list/agriculture-value-added-per-worker-constant-2000-us-dollar-wb-data.html
        router.get("/api/TE/WorldBank/Agriculture/AgricultureValueAddedPerWorkerConstant2000UsDollarWb").handler(this::extractDataWorldBankAgricultureAgricultureValueAddedPerWorkerConstant2000UsDollarWb);

        //This router permits to use an API to display the Arable land (% of land area)
        //from the URL : https://tradingeconomics.com/country-list/arable-land-percent-of-land-area-wb-data.html
        router.get("/api/TE/WorldBank/Agriculture/ArableLandPercentOfLandAreaWb").handler(this::extractDataWorldBankAgricultureArableLandPercentOfLandAreaWb);

        //This router permits to use an API to display the Arable land (hectares per person)
        //from the URL : https://tradingeconomics.com/country-list/arable-land-hectares-per-person-wb-data.html
        router.get("/api/TE/WorldBank/Agriculture/ArableLandHectaresPerPersonWb").handler(this::extractDataWorldBankAgricultureArableLandHectaresPerPersonWb);

        //This router permits to use an API to display the Average precipitation in depth (mm per year)
        //from the URL : https://tradingeconomics.com/country-list/average-precipitation-in-depth-mm-per-year-wb-data.html
        router.get("/api/TE/WorldBank/Agriculture/AveragePrecipitationInDepthMmPerYearWb").handler(this::extractDataWorldBankAgricultureAveragePrecipitationInDepthMmPerYearWb);

        //This router permits to use an API to display the Average tariffs imposed by developed countries on agricultural products from least developed countries
        //from the URL : https://tradingeconomics.com/country-list/average-tariffs-imposed-by-developed-countries-on-agricultural-products-from-least-developed-countries-wb-data.html
        router.get("/api/TE/WorldBank/Agriculture/AverageTariffsImposedByDevelopedCountriesOnAgriculturalProductsFromLeastDevelopedCountriesWb")
                .handler(this::extractDataWorldBankAgricultureAverageTariffsImposedByDevelopedCountriesOnAgriculturalProductsFromLeastDevelopedCountriesWb);

        //This router permits to use an API to display the Cereal yield (kg per hectare)
        //from the URL : https://tradingeconomics.com/country-list/cereal-yield-kg-per-hectare-wb-data.html
        router.get("/api/TE/WorldBank/Agriculture/CerealYieldKgPerHectareWb").handler(this::extractDataWorldBankAgricultureCerealYieldKgPerHectareWb);

        //This router permits to use an API to display the Employees, agriculture, female (% of female employment)
        //from the URL : https://tradingeconomics.com/country-list/employees-agriculture-female-percent-of-female-employment-wb-data.html
        router.get("/api/TE/WorldBank/Agriculture/EmployeesAgricultureFemalePercentOfFemaleEmploymentWb").handler(this::extractDataWorldBankAgricultureEmployeesAgricultureFemalePercentOfFemaleEmploymentWb);

        //This router permits to use an API to display the Employment in agriculture (% of total employment)
        //from the URL : https://tradingeconomics.com/country-list/employment-in-agriculture-percent-of-total-employment-wb-data.html
        router.get("/api/TE/WorldBank/Agriculture/EmploymentInAgriculturePercentOfTotalEmploymentWb").handler(this::extractDataWorldBankAgricultureEmploymentInAgriculturePercentOfTotalEmploymentWb);

        //This router permits to use an API to display the Fertilizer consumption (kilograms per hectare of arable land)
        //from the URL : https://tradingeconomics.com/country-list/fertilizer-consumption-kilograms-per-hectare-of-arable-land-wb-data.html
        router.get("/api/TE/WorldBank/Agriculture/FertilizerConsumptionKilogramsPerHectareOfArableLandWb").handler(this::extractDataWorldBankAgricultureFertilizerConsumptionKilogramsPerHectareOfArableLandWb);

        //This router permits to use an API to display the Forest area (% of land area)
        //from the URL : https://tradingeconomics.com/country-list/forest-area-percent-of-land-area-wb-data.html
        router.get("/api/TE/WorldBank/Agriculture/ForestAreaPercentOfLandAreaWb").handler(this::extractDataWorldBankAgricultureForestAreaPercentOfLandAreaWb);

        //This router permits to use an API to display the Land area (sq. km)
        //from the URL : https://tradingeconomics.com/country-list/land-area-sq-km-wb-data.html
        router.get("/api/TE/WorldBank/Agriculture/LandAreaSqKmWb").handler(this::extractDataWorldBankAgricultureLandAreaSqKmWb);

        //This router permits to use an API to display the Livestock production index (1999-2001 = 100)
        //from the URL : https://tradingeconomics.com/country-list/livestock-production-index-1999-2001--100-wb-data.html
        router.get("/api/TE/WorldBank/Agriculture/LiveStockProductionIndex1999_2001_100Wb").handler(this::extractDataWorldBankAgricultureLiveStockProductionIndex1999_2001_100Wb);

        //This router permits to use an API to display the Poverty gap at rural poverty line
        //from the URL : https://tradingeconomics.com/country-list/poverty-gap-at-rural-poverty-line-percent-wb-data.html
        router.get("/api/TE/WorldBank/Agriculture/PovertyGapAtRuralPovertyLinePercentWb").handler(this::extractDataWorldBankAgriculturePovertyGapAtRuralPovertyLinePercentWb);

        //This router permits to use an API to display the Real agricultural GDP per capita growth rate
        //from the URL : https://tradingeconomics.com/country-list/real-agricultural-gdp-per-capita-growth-rate-wb-data.html
        router.get("/api/TE/WorldBank/Agriculture/RealAgriculturalGdpPerCapitaGrowthRateWb").handler(this::extractDataWorldBankAgricultureRealAgriculturalGdpPerCapitaGrowthRateWb);

        //This router permits to use an API to display the Rural land area where elevation is below 5 meters (% of total land area)
        //from the URL : https://tradingeconomics.com/country-list/rural-land-area-where-elevation-is-below-5-meters-percent-of-total-land-area-wb-data.html
        router.get("/api/TE/WorldBank/Agriculture/RuralLandAreaWhereElevationIsBelow5MetersPercentOfTotalLandAreaWb")
                .handler(this::extractDataWorldBankAgricultureRuralLandAreaWhereElevationIsBelow5MetersPercentOfTotalLandAreaWb);

        //This router permits to use an API to display the Surface area (sq. km)
        //from the URL : https://tradingeconomics.com/country-list/surface-area-sq-km-wb-data.html
        router.get("/api/TE/WorldBank/Agriculture/SurfaceAreaSqKmWb").handler(this::extractDataWorldBankAgricultureSurfaceAreaSqKmWb);

        //This router permits to use an API to display the Total agricultural exports (FAO, current US$)
        //from the URL : https://tradingeconomics.com/country-list/total-agricultural-exports-fao-us-dollar-wb-data.html
        router.get("/api/TE/WorldBank/Agriculture/TotalAgriculturalExportsFaoUsDollarWb").handler(this::extractDataWorldBankAgricultureTotalAgriculturalExportsFaoUsDollarWb);

        ////////////////////////////////////////////////////////////////////////////////////////////////////////////////
        //Agriculture//

        //Demographics//
        ////////////////////////////////////////////////////////////////////////////////////////////////////////////////

        //This router permits to use an API to display the Access to a mobile phone or internet at home (% age 15+)
        //from the URL : https://tradingeconomics.com/country-list/access-to-a-mobile-phone-or-internet-at-home-percent-age-15-wb-data.html
        router.get("/api/TE/WorldBank/Demographics/AccessToAMobilePhoneOrInternetAtHomePercentAge15Wb").handler(this::extractDataWorldBankDemographicsAccessToAMobilePhoneOrInternetAtHomePercentAge15Wb);

        //This router permits to use an API to display the Access to a mobile phone or internet at home, income, poorest 40% (% age 15+)
        //from the URL : https://tradingeconomics.com/country-list/access-to-a-mobile-phone-or-internet-at-home-income-poorest-40percent-percent-age-15-wb-data.html
        router.get("/api/TE/WorldBank/Demographics/AccessToAMobilePhoneOrInternetAtHomeIncomePoorest40PercentPercentAge15Wb")
                .handler(this::extractDataWorldBankDemographicsAccessToAMobilePhoneOrInternetAtHomeIncomePoorest40PercentPercentAge15Wb);

        //This router permits to use an API to display the Access to a mobile phone or internet at home, male (% age 15+)
        //from the URL : https://tradingeconomics.com/country-list/access-to-a-mobile-phone-or-internet-at-home-male-percent-age-15-wb-data.html
        router.get("/api/TE/WorldBank/Demographics/AccessToAMobilePhoneOrInternetAtHomeMalePercentAge15Wb")
                .handler(this::extractDataWorldBankDemographicsAccessToAMobilePhoneOrInternetAtHomeMalePercentAge15Wb);

        //This router permits to use an API to display the Access to a mobile phone or internet at home, young adults (% ages 15-34)
        //from the URL : https://tradingeconomics.com/country-list/access-to-a-mobile-phone-or-internet-at-home-young-adults-percent-ages-15-34-wb-data.html
        router.get("/api/TE/WorldBank/Demographics/AccessToAMobilePhoneOrInternetAtHomeYoungAdultsPercentAges15_34Wb")
                .handler(this::extractDataWorldBankDemographicsAccessToAMobilePhoneOrInternetAtHomeYoungAdultsPercentAges15_34Wb);

        //This router permits to use an API to display the Access to an improved water source, rural (% of rural population): Q1 (lowest)
        //from the URL : https://tradingeconomics.com/country-list/access-to-an-improved-water-source-rural-percent-of-rural-population-q1-lowest-wb-data.html
        router.get("/api/TE/WorldBank/Demographics/AccessToAnImprovedWaterSourceRuralPercentOfRuralPopulationQ1LowestWb")
                .handler(this::extractDataWorldBankDemographicsAccessToAnImprovedWaterSourceRuralPercentOfRuralPopulationQ1LowestWb);

        //This router permits to use an API to display the Access to an improved water source, rural (% of rural population): Q3
        //from the URL : https://tradingeconomics.com/country-list/access-to-an-improved-water-source-rural-percent-of-rural-population-q3-wb-data.html
        router.get("/api/TE/WorldBank/Demographics/AccessToAnImprovedWaterSourceRuralPercentOfRuralPopulationQ3Wb")
                .handler(this::extractDataWorldBankDemographicsAccessToAnImprovedWaterSourceRuralPercentOfRuralPopulationQ3Wb);

        //This router permits to use an API to display the Access to an improved water source, urban : Q1 (lowest)
        //from the URL : https://tradingeconomics.com/country-list/access-to-an-improved-water-source-urban-q1-lowest-wb-data.html
        router.get("/api/TE/WorldBank/Demographics/AccessToAnImprovedWaterSourceUrbanQ1LowestWb")
                .handler(this::extractDataWorldBankDemographicsAccessToAnImprovedWaterSourceUrbanQ1LowestWb);

        //This router permits to use an API to display the Access to an improved water source, urban : Q3
        //from the URL : https://tradingeconomics.com/country-list/access-to-an-improved-water-source-urban-q3-wb-data.html
        router.get("/api/TE/WorldBank/Demographics/AccessToAnImprovedWaterSourceUrbanQ3Wb")
                .handler(this::extractDataWorldBankDemographicsAccessToAnImprovedWaterSourceUrbanQ3Wb);

        //This router permits to use an API to display the Access to an improved water source, urban : Q5 (highest)
        //from the URL : https://tradingeconomics.com/country-list/access-to-an-improved-water-source-urban-q5-highest-wb-data.html
        router.get("/api/TE/WorldBank/Demographics/AccessToAnImprovedWaterSourceUrbanQ5HighestWb")
                .handler(this::extractDataWorldBankDemographicsAccessToAnImprovedWaterSourceUrbanQ5HighestWb);

        //This router permits to use an API to display the Access to electricity
        //from the URL : https://tradingeconomics.com/country-list/access-to-electricity-percent-of-total-population-wb-data.html
        router.get("/api/TE/WorldBank/Demographics/AccessToElectricityPercentOfTotalPopulationWb")
                .handler(this::extractDataWorldBankDemographicsAccessToElectricityPercentOfTotalPopulationWb);

        //This router permits to use an API to display the Access to electricity (% of population)
        //from the URL : https://tradingeconomics.com/country-list/access-to-electricity-percent-of-population-wb-data.html
        router.get("/api/TE/WorldBank/Demographics/AccessToElectricityPercentOfPopulationWb")
                .handler(this::extractDataWorldBankDemographicsAccessToElectricityPercentOfPopulationWb);

        //This router permits to use an API to display the Access to electricity, rural (% of rural population)
        //from the URL : https://tradingeconomics.com/country-list/access-to-electricity-rural-percent-of-rural-population-wb-data.html
        router.get("/api/TE/WorldBank/Demographics/AccessToElectricityRuralPercentOfRuralPopulationWb")
                .handler(this::extractDataWorldBankDemographicsAccessToElectricityRuralPercentOfRuralPopulationWb);

        //This router permits to use an API to display the Access to finance (% of firms identifying this as a major constraint)
        //from the URL : https://tradingeconomics.com/country-list/access-to-finance-percent-of-firms-identifying-this-as-a-major-constraint-wb-data.html
        router.get("/api/TE/WorldBank/Demographics/AccessToFinancePercentOfFirmsIdentifyingThisAsAMajorConstraintWb")
                .handler(this::extractDataWorldBankDemographicsAccessToFinancePercentOfFirmsIdentifyingThisAsAMajorConstraintWb);

        //This router permits to use an API to display the Access to improved sanitation facilities, rural (% of rural population): Q2
        //from the URL : https://tradingeconomics.com/country-list/access-to-improved-sanitation-facilities-rural-percent-of-rural-population-q2-wb-data.html
        router.get("/api/TE/WorldBank/Demographics/AccessToImprovedSanitationFacilitiesRuralPercentOfRuralPopulationQ2Wb")
                .handler(this::extractDataWorldBankDemographicsAccessToImprovedSanitationFacilitiesRuralPercentOfRuralPopulationQ2Wb);

        //This router permits to use an API to display the Access to improved sanitation facilities, rural (% of rural population): Q4
        //from the URL : https://tradingeconomics.com/country-list/access-to-improved-sanitation-facilities-rural-percent-of-rural-population-q4-wb-data.html
        router.get("/api/TE/WorldBank/Demographics/AccessToImprovedSanitationFacilitiesRuralPercentOfRuralPopulationQ4Wb")
                .handler(this::extractDataWorldBankDemographicsAccessToImprovedSanitationFacilitiesRuralPercentOfRuralPopulationQ4Wb);

        //This router permits to use an API to display the Access to improved sanitation facilities, urban : Q1 (lowest)
        //from the URL : https://tradingeconomics.com/country-list/access-to-improved-sanitation-facilities-urban-q1-lowest-wb-data.html
        router.get("/api/TE/WorldBank/Demographics/AccessToImprovedSanitationFacilitiesUrbanQ1LowestWb").handler(this::extractDataWorldBankDemographicsAccessToImprovedSanitationFacilitiesUrbanQ1LowestWb);

        //This router permits to use an API to display the Access to improved sanitation facilities, urban : Q4
        //from the URL : https://tradingeconomics.com/country-list/access-to-improved-sanitation-facilities-urban-q4-wb-data.html
        router.get("/api/TE/WorldBank/Demographics/AccessToImprovedSanitationFacilitiesUrbanQ4Wb").handler(this::extractDataWorldBankDemographicsAccessToImprovedSanitationFacilitiesUrbanQ4Wb);

        //This router permits to use an API to display the Access to Land (% of managers surveyed ranking this as a major constraint)
        //from the URL : https://tradingeconomics.com/country-list/access-to-land-percent-of-managers-surveyed-ranking-this-as-a-major-constraint-wb-data.html
        router.get("/api/TE/WorldBank/Demographics/AccessToLandPercentOfManagersSurveyedRankingThisAsAMajorConstraintWb")
                .handler(this::extractDataWorldBankDemographicsAccessToLandPercentOfManagersSurveyedRankingThisAsAMajorConstraintWb);

        //This router permits to use an API to display the Access to Non-Solid Fuel (% of rural population)
        //from the URL : https://tradingeconomics.com/country-list/access-to-non-solid-fuel-percent-of-rural-population-wb-data.html
        router.get("/api/TE/WorldBank/Demographics/AccessToNonSolidFuelPercentOfRuralPopulationWb").handler(this::extractDataWorldBankDemographicsAccessToNonSolidFuelPercentOfRuralPopulationWb);

        //This router permits to use an API to display the Age dependency ratio (% of working-age population)
        //from the URL : https://tradingeconomics.com/country-list/age-dependency-ratio-percent-of-working-age-population-wb-data.html
        router.get("/api/TE/WorldBank/Demographics/AgeDependencyRatioPercentOfWorkingAgePopulationWb").handler(this::extractDataWorldBankDemographicsAgeDependencyRatioPercentOfWorkingAgePopulationWb);

        //This router permits to use an API to display the Age dependency ratio, young (% of working-age population)
        //from the URL : https://tradingeconomics.com/country-list/age-dependency-ratio-young-percent-of-working-age-population-wb-data.html
        router.get("/api/TE/WorldBank/Demographics/AgeDependencyRatioYoungPercentOfWorkingAgePopulationWb").handler(this::extractDataWorldBankDemographicsAgeDependencyRatioYoungPercentOfWorkingAgePopulationWb);

        //This router permits to use an API to display the Age population, age 07, female, interpolated
        //from the URL : https://tradingeconomics.com/country-list/age-population-age-07-female-interpolated-wb-data.html
        router.get("/api/TE/WorldBank/Demographics/AgePopulationAge07FemaleInterpolatedWb").handler(this::extractDataWorldBankDemographicsAgePopulationAge07FemaleInterpolatedWb);

        //This router permits to use an API to display the Age population, age 08, female, interpolated
        //from the URL : https://tradingeconomics.com/country-list/age-population-age-08-female-interpolated-wb-data.html
        router.get("/api/TE/WorldBank/Demographics/AgePopulationAge08FemaleInterpolatedWb").handler(this::extractDataWorldBankDemographicsAgePopulationAge08FemaleInterpolatedWb);

        //This router permits to use an API to display the Age population, age 09, female, interpolated
        //from the URL : https://tradingeconomics.com/country-list/age-population-age-09-female-interpolated-wb-data.html
        router.get("/api/TE/WorldBank/Demographics/AgePopulationAge09FemaleInterpolatedWb").handler(this::extractDataWorldBankDemographicsAgePopulationAge09FemaleInterpolatedWb);

        //This router permits to use an API to display the Age population, age 10, female, interpolated
        //from the URL : https://tradingeconomics.com/country-list/age-population-age-10-female-interpolated-wb-data.html
        router.get("/api/TE/WorldBank/Demographics/AgePopulationAge10FemaleInterpolatedWb").handler(this::extractDataWorldBankDemographicsAgePopulationAge10FemaleInterpolatedWb);

        //This router permits to use an API to display the Age population, age 11, female, interpolated
        //from the URL : https://tradingeconomics.com/country-list/age-population-age-11-female-interpolated-wb-data.html
        router.get("/api/TE/WorldBank/Demographics/AgePopulationAge11FemaleInterpolatedWb").handler(this::extractDataWorldBankDemographicsAgePopulationAge11FemaleInterpolatedWb);

        //This router permits to use an API to display the Age population, age 12, female, interpolated
        //from the URL : https://tradingeconomics.com/country-list/age-population-age-12-female-interpolated-wb-data.html
        router.get("/api/TE/WorldBank/Demographics/AgePopulationAge12FemaleInterpolatedWb").handler(this::extractDataWorldBankDemographicsAgePopulationAge12FemaleInterpolatedWb);

        //This router permits to use an API to display the Age population, age 13, female, interpolated
        //from the URL : https://tradingeconomics.com/country-list/age-population-age-13-female-interpolated-wb-data.html
        router.get("/api/TE/WorldBank/Demographics/AgePopulationAge13FemaleInterpolatedWb").handler(this::extractDataWorldBankDemographicsAgePopulationAge13FemaleInterpolatedWb);

        //This router permits to use an API to display the Age population, age 14, female, interpolated
        //from the URL : https://tradingeconomics.com/country-list/age-population-age-14-female-interpolated-wb-data.html
        router.get("/api/TE/WorldBank/Demographics/AgePopulationAge14FemaleInterpolatedWb").handler(this::extractDataWorldBankDemographicsAgePopulationAge14FemaleInterpolatedWb);

        //This router permits to use an API to display the Age population, age 15, female, interpolated
        //from the URL : https://tradingeconomics.com/country-list/age-population-age-15-female-interpolated-wb-data.html
        router.get("/api/TE/WorldBank/Demographics/AgePopulationAge15FemaleInterpolatedWb").handler(this::extractDataWorldBankDemographicsAgePopulationAge15FemaleInterpolatedWb);

        //This router permits to use an API to display the Age population, age 16, female, interpolated
        //from the URL : https://tradingeconomics.com/country-list/age-population-age-16-female-interpolated-wb-data.html
        router.get("/api/TE/WorldBank/Demographics/AgePopulationAge16FemaleInterpolatedWb").handler(this::extractDataWorldBankDemographicsAgePopulationAge16FemaleInterpolatedWb);

        //This router permits to use an API to display the Age population, age 17, female, interpolated
        //from the URL : https://tradingeconomics.com/country-list/age-population-age-17-female-interpolated-wb-data.html
        router.get("/api/TE/WorldBank/Demographics/AgePopulationAge17FemaleInterpolatedWb").handler(this::extractDataWorldBankDemographicsAgePopulationAge17FemaleInterpolatedWb);

        //This router permits to use an API to display the Age population, age 18, female, interpolated
        //from the URL : https://tradingeconomics.com/country-list/age-population-age-18-female-interpolated-wb-data.html
        router.get("/api/TE/WorldBank/Demographics/AgePopulationAge18FemaleInterpolatedWb").handler(this::extractDataWorldBankDemographicsAgePopulationAge18FemaleInterpolatedWb);

        //This router permits to use an API to display the Age population, age 19, female, interpolated
        //from the URL : https://tradingeconomics.com/country-list/age-population-age-19-female-interpolated-wb-data.html
        router.get("/api/TE/WorldBank/Demographics/AgePopulationAge19FemaleInterpolatedWb").handler(this::extractDataWorldBankDemographicsAgePopulationAge19FemaleInterpolatedWb);

        //This router permits to use an API to display the Age population, age 20, female, interpolated
        //from the URL : https://tradingeconomics.com/country-list/age-population-age-20-female-interpolated-wb-data.html
        router.get("/api/TE/WorldBank/Demographics/AgePopulationAge20FemaleInterpolatedWb").handler(this::extractDataWorldBankDemographicsAgePopulationAge20FemaleInterpolatedWb);

        //This router permits to use an API to display the Age population, age 21, female, interpolated
        //from the URL : https://tradingeconomics.com/country-list/age-population-age-21-female-interpolated-wb-data.html
        router.get("/api/TE/WorldBank/Demographics/AgePopulationAge21FemaleInterpolatedWb").handler(this::extractData);

        //This router permits to use an API to display the Age population, age 22, female, interpolated
        //from the URL : https://tradingeconomics.com/country-list/age-population-age-22-female-interpolated-wb-data.html
        router.get("/api/TE/WorldBank/Demographics/AgePopulationAge22FemaleInterpolatedWb").handler(this::extractDataWorldBankDemographicsAgePopulationAge22FemaleInterpolatedWb);

        //This router permits to use an API to display the Age population, age 23, female, interpolated
        //from the URL : https://tradingeconomics.com/country-list/age-population-age-23-female-interpolated-wb-data.html
        router.get("/api/TE/WorldBank/Demographics/AgePopulationAge23FemaleInterpolatedWb").handler(this::extractDataWorldBankDemographicsAgePopulationAge23FemaleInterpolatedWb);

        //This router permits to use an API to display the Age population, age 24, female, interpolated
        //from the URL : https://tradingeconomics.com/country-list/age-population-age-24-female-interpolated-wb-data.html
        router.get("/api/TE/WorldBank/Demographics/AgePopulationAge24FemaleInterpolatedWb").handler(this::extractDataWorldBankDemographicsAgePopulationAge24FemaleInterpolatedWb);

        //This router permits to use an API to display the Age population, age 25, female, interpolated
        //from the URL : https://tradingeconomics.com/country-list/age-population-age-25-female-interpolated-wb-data.html
        router.get("/api/TE/WorldBank/Demographics/AgePopulationAge25FemaleInterpolatedWb").handler(this::extractDataWorldBankDemographicsAgePopulationAge25FemaleInterpolatedWb);

        //This router permits to use an API to display the Agricultural population (FAO, number)
        //from the URL : https://tradingeconomics.com/country-list/agricultural-population-fao-number-wb-data.html
        router.get("/api/TE/WorldBank/Demographics/AgriculturalPopulationFaoNumberWb").handler(this::extractDataWorldBankDemographicsAgriculturalPopulationFaoNumberWb);

        //This router permits to use an API to display the Annualized average growth rate in per capita
        //real survey mean consumption or income, total population
        //from the URL : https://tradingeconomics.com/country-list/annualized-average-growth-rate-in-per-capita-real-survey-mean-consumption-or-income-total-population-wb-data.html
        router.get("/api/TE/WorldBank/Demographics/AnnualizedAverageGrowthRateInPerCapitaRealSurveyMeanConsumptionOrIncomeTotalPopulationWb")
                .handler(this::extractDataWorldBankDemographicsAnnualizedAverageGrowthRateInPerCapitaRealSurveyMeanConsumptionOrIncomeTotalPopulationWb);

        //This router permits to use an API to display the Condom use; population ages 15-24; male (% of males ages 15-24)
        //from the URL : https://tradingeconomics.com/country-list/condom-use-population-ages-15-24-male-percent-of-males-ages-15-24-wb-data.html
        router.get("/api/TE/WorldBank/Demographics/CondomUsePopulationAges15_24MalePercentOfMalesAges15_24Wb")
                .handler(this::extractDataWorldBankDemographicsCondomUsePopulationAges15_24MalePercentOfMalesAges15_24Wb);

        //This router permits to use an API to display the Coverage of unemployment benefits and ALMP in 3rd quintile (% of population)
        //from the URL : https://tradingeconomics.com/country-list/coverage-of-unemployment-benefits-and-almp-in-3rd-quintile-percent-of-population-wb-data.html
        router.get("/api/TE/WorldBank/Demographics/CoverageOfUnemploymentBenefitsAndAlmpIn3rdQuintilePercentOfPopulationWb")
                .handler(this::extractDataWorldBankDemographicsCoverageOfUnemploymentBenefitsAndAlmpIn3rdQuintilePercentOfPopulationWb);

        //This router permits to use an API to display the Coverage of unemployment benefits and ALMP in richest quintile (% of population)
        //from the URL : https://tradingeconomics.com/country-list/coverage-of-unemployment-benefits-and-almp-in-richest-quintile-percent-of-population-wb-data.html
        router.get("/api/TE/WorldBank/Demographics/CoverageOfUnemploymentBenefitsAndAlmpInRichestQuintilePercentOfPopulationWb")
                .handler(this::extractDataWorldBankDemographicsCoverageOfUnemploymentBenefitsAndAlmpInRichestQuintilePercentOfPopulationWb);

        //This router permits to use an API to display the Diabetes prevalence (% of population ages 20 to 79)
        //from the URL : https://tradingeconomics.com/country-list/diabetes-prevalence-percent-of-population-ages-20-to-79-wb-data.html
        router.get("/api/TE/WorldBank/Demographics/DiabetesPrevalencePercentOfPopulationAges20_to_79Wb")
                .handler(this::extractDataWorldBankDemographicsDiabetesPrevalencePercentOfPopulationAges20_to_79Wb);

        //This router permits to use an API to display the Economically active population in agriculture
        //from the URL : https://tradingeconomics.com/country-list/economically-active-population-in-agriculture-number-wb-data.html
        router.get("/api/TE/WorldBank/Demographics/EconomicallyActivePopulationInAgricultureNumberWb")
                .handler(this::extractDataWorldBankDemographicsEconomicallyActivePopulationInAgricultureNumberWb);

        //This router permits to use an API to display the Economically active population in agriculture, male (FAO, number)
        //from the URL : https://tradingeconomics.com/country-list/economically-active-population-in-agriculture-male-fao-number-wb-data.html
        router.get("/api/TE/WorldBank/Demographics/EconomicallyActivePopulationInAgricultureMaleFaoNumberWb")
                .handler(this::extractDataWorldBankDemographicsEconomicallyActivePopulationInAgricultureMaleFaoNumberWb);

        //This router permits to use an API to display the Emigration rate of tertiary educated (% of total tertiary educated population)
        //from the URL : https://tradingeconomics.com/country-list/emigration-rate-of-tertiary-educated-percent-of-total-tertiary-educated-population-wb-data.html
        router.get("/api/TE/WorldBank/Demographics/EmigrationRateOfTertiaryEducatedPercentOfTotalTertiaryEducatedPopulationWb")
                .handler(this::extractDataWorldBankDemographicsEmigrationRateOfTertiaryEducatedPercentOfTotalTertiaryEducatedPopulationWb);

        //This router permits to use an API to display the Employment to population ratio, 15+, male
        //from the URL : https://tradingeconomics.com/country-list/employment-to-population-ratio-15-male-percent-wb-data.html
        router.get("/api/TE/WorldBank/Demographics/EmploymentToPopulationRatio15MalePercentWb")
                .handler(this::extractDataWorldBankDemographicsEmploymentToPopulationRatio15MalePercentWb);

        //This router permits to use an API to display the Employment to population ratio, 15+, total
        //from the URL : https://tradingeconomics.com/country-list/employment-to-population-ratio-15-total-percent-wb-data.html
        router.get("/api/TE/WorldBank/Demographics/EmploymentToPopulationRatio15TotalPercentWb")
                .handler(this::extractDataWorldBankDemographicsEmploymentToPopulationRatio15TotalPercentWb);

        //This router permits to use an API to display the Employment to population ratio, ages 15-24, female
        //from the URL : https://tradingeconomics.com/country-list/employment-to-population-ratio-ages-15-24-female-percent-wb-data.html
        router.get("/api/TE/WorldBank/Demographics/EmploymentToPopulationRatioAges15_24FemalePercentWb")
                .handler(this::extractDataWorldBankDemographicsEmploymentToPopulationRatioAges15_24FemalePercentWb);

        //This router permits to use an API to display the Employment to population ratio, ages 15-24, male
        //from the URL : https://tradingeconomics.com/country-list/employment-to-population-ratio-ages-15-24-male-percent-wb-data.html
        router.get("/api/TE/WorldBank/Demographics/EmploymentToPopulationRatioAges15_24MalePercentWb")
                .handler(this::extractDataWorldBankDemographicsEmploymentToPopulationRatioAges15_24MalePercentWb);

        //This router permits to use an API to display the Employment to population ratio, ages 15-24, total
        //from the URL : https://tradingeconomics.com/country-list/employment-to-population-ratio-ages-15-24-total-percent-wb-data.html
        router.get("/api/TE/WorldBank/Demographics/EmploymentToPopulationRatioAges15_24TotalPercentWb")
                .handler(this::extractDataWorldBankDemographicsEmploymentToPopulationRatioAges15_24TotalPercentWb);

        //This router permits to use an API to display the Female population 00-04
        //from the URL : https://tradingeconomics.com/country-list/female-population-00-04-wb-data.html
        router.get("/api/TE/WorldBank/Demographics/FemalePopulation00_04Wb").handler(this::extractDataWorldBankDemographicsFemalePopulation00_04Wb);

        //This router permits to use an API to display the Female population 10-14
        //from the URL : https://tradingeconomics.com/country-list/female-population-10-14-wb-data.html
        router.get("/api/TE/WorldBank/Demographics/FemalePopulation10_14Wb").handler(this::extractDataWorldBankDemographicsFemalePopulation10_14Wb);

        //This router permits to use an API to display the Female population 20-24
        //from the URL : https://tradingeconomics.com/country-list/female-population-20-24-wb-data.html
        router.get("/api/TE/WorldBank/Demographics/FemalePopulation20_24Wb").handler(this::extractDataWorldBankDemographicsFemalePopulation20_24Wb);

        //This router permits to use an API to display the Female population 30-34
        //from the URL : https://tradingeconomics.com/country-list/female-population-30-34-wb-data.html
        router.get("/api/TE/WorldBank/Demographics/FemalePopulation30_34Wb").handler(this::extractDataWorldBankDemographicsFemalePopulation30_34Wb);

        //This router permits to use an API to display the Female population 40-44
        //from the URL : https://tradingeconomics.com/country-list/female-population-40-44-wb-data.html
        router.get("/api/TE/WorldBank/Demographics/FemalePopulation40_44Wb").handler(this::extractDataWorldBankDemographicsFemalePopulation40_44Wb);

        //This router permits to use an API to display the Female population 50-54
        //from the URL : https://tradingeconomics.com/country-list/female-population-50-54-wb-data.html
        router.get("/api/TE/WorldBank/Demographics/FemalePopulation50_54Wb").handler(this::extractDataWorldBankDemographicsFemalePopulation50_54Wb);

        //This router permits to use an API to display the Female population 60-64
        //from the URL : https://tradingeconomics.com/country-list/female-population-60-64-wb-data.html
        router.get("/api/TE/WorldBank/Demographics/FemalePopulation60_64Wb").handler(this::extractDataWorldBankDemographicsFemalePopulation60_64Wb);

        //This router permits to use an API to display the Female population 70-74
        //from the URL : https://tradingeconomics.com/country-list/female-population-70-74-wb-data.html
        router.get("/api/TE/WorldBank/Demographics/FemalePopulation70_74Wb").handler(this::extractDataWorldBankDemographicsFemalePopulation70_74Wb);

        //This router permits to use an API to display the Government Hospitals Number of beds Per 100,000 Population
        //from the URL : https://tradingeconomics.com/country-list/government-hospitals-number-of-beds-per-100-000-population-wb-data.html
        router.get("/api/TE/WorldBank/Demographics/GovernmentHospitalsNumberOfBedsPer100000PopulationWb")
                .handler(this::extractDataWorldBankDemographicsGovernmentHospitalsNumberOfBedsPer100000PopulationWb);

        //This router permits to use an API to display the Immunization Coverage for Children under 5 years old (in % of children population under 5 years old)
        //from the URL : https://tradingeconomics.com/country-list/immunization-coverage-for-children-under-5-years-old-in-percent-of-children-population-under-5-years-old-wb-data.html
        router.get("/api/TE/WorldBank/Demographics/ImmunizationCoverageForChildrenUnder5YearsOldInPercentOfChildrenPopulationUnder5YearsOldWb")
                .handler(this::extractDataWorldBankDemographicsImmunizationCoverageForChildrenUnder5YearsOldInPercentOfChildrenPopulationUnder5YearsOldWb);

        //This router permits to use an API to display the Improved sanitation facilities, rural (% of rural population with access)
        //from the URL : https://tradingeconomics.com/country-list/improved-sanitation-facilities-rural-percent-of-rural-population-with-access-wb-data.html
        router.get("/api/TE/WorldBank/Demographics/ImprovedSanitationFacilitiesRuralPercentOfRuralPopulationWithAccessWb")
                .handler(this::extractDataWorldBankDemographicsImprovedSanitationFacilitiesRuralPercentOfRuralPopulationWithAccessWb);

        //This router permits to use an API to display the Improved water source (% of population with access)
        //from the URL : https://tradingeconomics.com/country-list/improved-water-source-percent-of-population-with-access-wb-data.html
        router.get("/api/TE/WorldBank/Demographics/ImprovedWaterSourcePercentOfPopulationWithAccessWb")
                .handler(this::extractDataWorldBankDemographicsImprovedWaterSourcePercentOfPopulationWithAccessWb);

        //This router permits to use an API to display the Improved water source, urban (% of urban population with access)
        //from the URL : https://tradingeconomics.com/country-list/improved-water-source-urban-percent-of-urban-population-with-access-wb-data.html
        router.get("/api/TE/WorldBank/Demographics/ImprovedWaterSourceUrbanPercentOfUrbanPopulationWithAccessWb")
                .handler(this::extractDataWorldBankDemographicsImprovedWaterSourceUrbanPercentOfUrbanPopulationWithAccessWb);

        //This router permits to use an API to display the International migrant stock (% of population)
        //from the URL : https://tradingeconomics.com/country-list/international-migrant-stock-percent-of-population-wb-data.html
        router.get("/api/TE/WorldBank/Demographics/InternationalMigrantStockPercentOfPopulationWb")
                .handler(this::extractDataWorldBankDemographicsInternationalMigrantStockPercentOfPopulationWb);

        //This router permits to use an API to display the Male population 05-09
        //from the URL : https://tradingeconomics.com/country-list/male-population-05-09-wb-data.html
        router.get("/api/TE/WorldBank/Demographics/MalePopulation05_09Wb").handler(this::extractDataWorldBankDemographicsMalePopulation05_09Wb);

        //This router permits to use an API to display the Male population 15-19
        //from the URL : https://tradingeconomics.com/country-list/male-population-15-19-wb-data.html
        router.get("/api/TE/WorldBank/Demographics/MalePopulation15_19Wb").handler(this::extractDataWorldBankDemographicsMalePopulation15_19Wb);

        //This router permits to use an API to display the Male population 25-29
        //from the URL : https://tradingeconomics.com/country-list/male-population-25-29-wb-data.html
        router.get("/api/TE/WorldBank/Demographics/MalePopulation25_29Wb").handler(this::extractDataWorldBankDemographicsMalePopulation25_29Wb);

        //This router permits to use an API to display the Male population 35-39
        //from the URL : https://tradingeconomics.com/country-list/male-population-35-39-wb-data.html
        router.get("/api/TE/WorldBank/Demographics/MalePopulation35_39Wb").handler(this::extractDataWorldBankDemographicsMalePopulation35_39Wb);

        //This router permits to use an API to display the Male population 45-49
        //from the URL : https://tradingeconomics.com/country-list/male-population-45-49-wb-data.html
        router.get("/api/TE/WorldBank/Demographics/MalePopulation45_49Wb").handler(this::extractDataWorldBankDemographicsMalePopulation45_49Wb);

        //This router permits to use an API to display the Male population 55-59
        //from the URL : https://tradingeconomics.com/country-list/male-population-55-59-wb-data.html
        router.get("/api/TE/WorldBank/Demographics/MalePopulation55_59Wb").handler(this::extractDataWorldBankDemographicsMalePopulation55_59Wb);

        //This router permits to use an API to display the Male population 65-69
        //from the URL : https://tradingeconomics.com/country-list/male-population-65-69-wb-data.html
        router.get("/api/TE/WorldBank/Demographics/MalePopulation65_69Wb").handler(this::extractDataWorldBankDemographicsMalePopulation65_69Wb);

        //This router permits to use an API to display the Male population 75-79
        //from the URL : https://tradingeconomics.com/country-list/male-population-75-79-wb-data.html
        router.get("/api/TE/WorldBank/Demographics/MalePopulation75_79Wb")
                .handler(this::extractDataWorldBankDemographicsMalePopulation75_79Wb);

        //This router permits to use an API to display the Male-female gap in the percent of population (15+)
        // with an account at a formal financial institution
        //from the URL : https://tradingeconomics.com/country-list/male-female-gap-in-the-percent-of-population-15-with-an-account-at-a-formal-financial-institution-wb-data.html
        router.get("/api/TE/WorldBank/Demographics/MaleFemaleGapInThePercentOfPopulation15WithAnAccountAtAFormalFinancialInstitutionWb")
                .handler(this::extractDataWorldBankDemographicsMaleFemaleGapInThePercentOfPopulation15WithAnAccountAtAFormalFinancialInstitutionWb);

        //This router permits to use an API to display the Number of surgical procedures (per 100,000 population)
        //from the URL : https://tradingeconomics.com/country-list/number-of-surgical-procedures-per-100-000-population-wb-data.html
        router.get("/api/TE/WorldBank/Demographics/NumberOfSurgicalProceduresPer100000PopulationWb")
                .handler(this::extractDataWorldBankDemographicsNumberOfSurgicalProceduresPer100000PopulationWb);

        //This router permits to use an API to display the People practicing open defecation, rural (% of rural population)
        //from the URL : https://tradingeconomics.com/country-list/people-practicing-open-defecation-rural-percent-of-rural-population-wb-data.html
        router.get("/api/TE/WorldBank/Demographics/PeoplePracticingOpenDefecationRuralPercentOfRuralPopulationWb")
                .handler(this::extractDataWorldBankDemographicsPeoplePracticingOpenDefecationRuralPercentOfRuralPopulationWb);

        //This router permits to use an API to display the People practicing open defecation, rural (% of rural population): Q2
        //from the URL : https://tradingeconomics.com/country-list/people-practicing-open-defecation-rural-percent-of-rural-population-q2-wb-data.html
        router.get("/api/TE/WorldBank/Demographics/PeoplePracticingOpenDefecationRuralPercentOfRuralPopulationQ2Wb")
                .handler(this::extractDataWorldBankDemographicsPeoplePracticingOpenDefecationRuralPercentOfRuralPopulationQ2Wb);

        //This router permits to use an API to display the People practicing open defecation, rural (% of rural population): Q4
        //from the URL : https://tradingeconomics.com/country-list/people-practicing-open-defecation-rural-percent-of-rural-population-q4-wb-data.html
        router.get("/api/TE/WorldBank/Demographics/PeoplePracticingOpenDefecationRuralPercentOfRuralPopulationQ4Wb")
                .handler(this::extractDataWorldBankDemographicsPeoplePracticingOpenDefecationRuralPercentOfRuralPopulationQ4Wb);

        //This router permits to use an API to display the People practicing open defecation, urban
        //from the URL : https://tradingeconomics.com/country-list/people-practicing-open-defecation-urban-wb-data.html
        router.get("/api/TE/WorldBank/Demographics/PeoplePracticingOpenDefecationUrbanWb")
                .handler(this::extractDataWorldBankDemographicsPeoplePracticingOpenDefecationUrbanWb);

        //This router permits to use an API to display the People practicing open defecation, urban : Q2
        //from the URL : https://tradingeconomics.com/country-list/people-practicing-open-defecation-urban-q2-wb-data.html
        router.get("/api/TE/WorldBank/Demographics/PeoplePracticingOpenDefecationUrbanQ2Wb")
                .handler(this::extractDataWorldBankDemographicsPeoplePracticingOpenDefecationUrbanQ2Wb);

        //This router permits to use an API to display the People practicing open defecation, urban : Q4
        //from the URL : https://tradingeconomics.com/country-list/people-practicing-open-defecation-urban-q4-wb-data.html
        router.get("/api/TE/WorldBank/Demographics/PeoplePracticingOpenDefecationUrbanQ4Wb")
                .handler(this::extractDataWorldBankDemographicsPeoplePracticingOpenDefecationUrbanQ4Wb);

        //This router permits to use an API to display the Percentage of Population in Urban Areas (in % of Total Population)
        //from the URL : https://tradingeconomics.com/country-list/percentage-of-population-in-urban-areas-in-percent-of-total-population-wb-data.html
        router.get("/api/TE/WorldBank/Demographics/PercentageOfPopulationInUrbanAreasInPercentOfTotalPopulationWb")
                .handler(this::extractDataWorldBankDemographicsPercentageOfPopulationInUrbanAreasInPercentOfTotalPopulationWb);

        //This router permits to use an API to display the Population (% of total)
        //from the URL : https://tradingeconomics.com/country-list/population-percent-of-total-wb-data.html
        router.get("/api/TE/WorldBank/Demographics/PopulationPercentOfTotalWb")
                .handler(this::extractDataWorldBankDemographicsPopulationPercentOfTotalWb);

        //This router permits to use an API to display the Population ages 0-14 (% of total)
        //from the URL : https://tradingeconomics.com/country-list/population-ages-0-14-percent-of-total-wb-data.html
        router.get("/api/TE/WorldBank/Demographics/PopulationAges0_14PercentOfTotalWb")
                .handler(this::extractDataWorldBankDemographicsPopulationAges0_14PercentOfTotalWb);

        //This router permits to use an API to display the Population ages 0-14, female (% of total)
        //from the URL : https://tradingeconomics.com/country-list/population-ages-0-14-female-percent-of-total-wb-data.html
        router.get("/api/TE/WorldBank/Demographics/PopulationAges0_14FemalePercentOfTotalWb")
                .handler(this::extractDataWorldBankDemographicsPopulationAges0_14FemalePercentOfTotalWb);

        //This router permits to use an API to display the Population ages 0-4, female (% of female population)
        //from the URL : https://tradingeconomics.com/country-list/population-ages-0-4-female-percent-of-female-population-wb-data.html
        router.get("/api/TE/WorldBank/Demographics/PopulationAges0_4FemalePercentOfFemalePopulationWb")
                .handler(this::extractDataWorldBankDemographicsPopulationAges0_4FemalePercentOfFemalePopulationWb);

        //This router permits to use an API to display the Population ages 10-14, female (% of female population)
        //from the URL : https://tradingeconomics.com/country-list/population-ages-10-14-female-percent-of-female-population-wb-data.html
        router.get("/api/TE/WorldBank/Demographics/PopulationAges10_14FemalePercentOfFemalePopulationWb")
                .handler(this::extractDataWorldBankDemographicsPopulationAges10_14FemalePercentOfFemalePopulationWb);

        //This router permits to use an API to display the Population ages 15-19, female (% of female population)
        //from the URL : https://tradingeconomics.com/country-list/population-ages-15-19-female-percent-of-female-population-wb-data.html
        router.get("/api/TE/WorldBank/Demographics/PopulationAges15_19FemalePercentOfFemalePopulationWb")
                .handler(this::extractDataWorldBankDemographicsPopulationAges15_19FemalePercentOfFemalePopulationWb);

        //This router permits to use an API to display the Population ages 15-64 (% of total)
        //from the URL : https://tradingeconomics.com/country-list/population-ages-15-64-percent-of-total-wb-data.html
        router.get("/api/TE/WorldBank/Demographics/PopulationAges15_64PercentOfTotalWb")
                .handler(this::extractDataWorldBankDemographicsPopulationAges15_64PercentOfTotalWb);

        //This router permits to use an API to display the Population ages 15-64, female (% of total)
        //from the URL : https://tradingeconomics.com/country-list/population-ages-15-64-female-percent-of-total-wb-data.html
        router.get("/api/TE/WorldBank/Demographics/PopulationAges15_64FemalePercentOfTotalWb")
                .handler(this::extractDataWorldBankDemographicsPopulationAges15_64FemalePercentOfTotalWb);

        //This router permits to use an API to display the Population ages 15-64, male (% of total)
        //from the URL : https://tradingeconomics.com/country-list/population-ages-15-64-male-percent-of-total-wb-data.html
        router.get("/api/TE/WorldBank/Demographics/PopulationAges15_64MalePercentOfTotalWb")
                .handler(this::extractDataWorldBankDemographicsPopulationAges15_64MalePercentOfTotalWb);

        //This router permits to use an API to display the Population ages 20-24, female (% of female population)
        //from the URL : https://tradingeconomics.com/country-list/population-ages-20-24-female-percent-of-female-population-wb-data.html
        router.get("/api/TE/WorldBank/Demographics/PopulationAges20_24FemalePercentOfFemalePopulationWb")
                .handler(this::extractDataWorldBankDemographicsPopulationAges20_24FemalePercentOfFemalePopulationWb);

        //This router permits to use an API to display the Population ages 25-29, female (% of female population)
        //from the URL : https://tradingeconomics.com/country-list/population-ages-25-29-female-percent-of-female-population-wb-data.html
        router.get("/api/TE/WorldBank/Demographics/PopulationAges25_29FemalePercentOfFemalePopulationWb")
                .handler(this::extractDataWorldBankDemographicsPopulationAges25_29FemalePercentOfFemalePopulationWb);

        //This router permits to use an API to display the Population ages 30-34, female (% of female population)
        //from the URL : https://tradingeconomics.com/country-list/population-ages-30-34-female-percent-of-female-population-wb-data.html
        router.get("/api/TE/WorldBank/Demographics/PopulationAges30_34FemalePercentOfFemalePopulationWb")
                .handler(this::extractDataWorldBankDemographicsPopulationAges30_34FemalePercentOfFemalePopulationWb);

        //This router permits to use an API to display the Population ages 35-39, female (% of female population)
        //from the URL : https://tradingeconomics.com/country-list/population-ages-35-39-female-percent-of-female-population-wb-data.html
        router.get("/api/TE/WorldBank/Demographics/PopulationAges35_39FemalePercentOfFemalePopulationWb")
                .handler(this::extractDataWorldBankDemographicsPopulationAges35_39FemalePercentOfFemalePopulationWb);

        //This router permits to use an API to display the Population ages 40-44, female (% of female population)
        //from the URL : https://tradingeconomics.com/country-list/population-ages-40-44-female-percent-of-female-population-wb-data.html
        router.get("/api/TE/WorldBank/Demographics/PopulationAges40_44FemalePercentOfFemalePopulationWb")
                .handler(this::extractDataWorldBankDemographicsPopulationAges40_44FemalePercentOfFemalePopulationWb);

        //This router permits to use an API to display the Population ages 45-49, female (% of female population)
        //from the URL : https://tradingeconomics.com/country-list/population-ages-45-49-female-percent-of-female-population-wb-data.html
        router.get("/api/TE/WorldBank/Demographics/PopulationAges45_49FemalePercentOfFemalePopulationWb")
                .handler(this::extractDataWorldBankDemographicsPopulationAges45_49FemalePercentOfFemalePopulationWb);

        //This router permits to use an API to display the Population ages 5-9, female (% of female population)
        //from the URL : https://tradingeconomics.com/country-list/population-ages-5-9-female-percent-of-female-population-wb-data.html
        router.get("/api/TE/WorldBank/Demographics/PopulationAges5_9FemalePercentOfFemalePopulationWb")
                .handler(this::extractDataWorldBankDemographicsPopulationAges5_9FemalePercentOfFemalePopulationWb);

        //This router permits to use an API to display the Population ages 50-54, female (% of female population)
        //from the URL : https://tradingeconomics.com/country-list/population-ages-50-54-female-percent-of-female-population-wb-data.html
        router.get("/api/TE/WorldBank/Demographics/PopulationAges50_54FemalePercentOfFemalePopulationWb")
                .handler(this::extractDataWorldBankDemographicsPopulationAges50_54FemalePercentOfFemalePopulationWb);

        //This router permits to use an API to display the Population ages 50-64, female (% of female population)
        //from the URL : https://tradingeconomics.com/country-list/population-ages-50-64-female-percent-of-female-population-wb-data.html
        router.get("/api/TE/WorldBank/Demographics/PopulationAges50_64FemalePercentOfFemalePopulationWb")
                .handler(this::extractDataWorldBankDemographicsPopulationAges50_64FemalePercentOfFemalePopulationWb);

        //This router permits to use an API to display the Population ages 55-59, female (% of female population)
        //from the URL : https://tradingeconomics.com/country-list/population-ages-55-59-female-percent-of-female-population-wb-data.html
        router.get("/api/TE/WorldBank/Demographics/PopulationAges55_59FemalePercentOfFemalePopulationWb")
                .handler(this::extractDataWorldBankDemographicsPopulationAges55_59FemalePercentOfFemalePopulationWb);

        //This router permits to use an API to display the Population ages 65 and above (% of total)
        //from the URL : https://tradingeconomics.com/country-list/population-ages-65-and-above-percent-of-total-wb-data.html
        router.get("/api/TE/WorldBank/Demographics/PopulationAges65AndAbovePercentOfTotalWb")
                .handler(this::extractDataWorldBankDemographicsPopulationAges65AndAbovePercentOfTotalWb);

        //This router permits to use an API to display the Population ages 65 and above, female (% of total)
        //from the URL : https://tradingeconomics.com/country-list/population-ages-65-and-above-female-percent-of-total-wb-data.html
        router.get("/api/TE/WorldBank/Demographics/PopulationAges65AndAboveFemalePercentOfTotalWb")
                .handler(this::extractDataWorldBankDemographicsPopulationAges65AndAboveFemalePercentOfTotalWb);

        //This router permits to use an API to display the Population ages 65 and above, male (% of total)
        //from the URL : https://tradingeconomics.com/country-list/population-ages-65-and-above-male-percent-of-total-wb-data.html
        router.get("/api/TE/WorldBank/Demographics/PopulationAges65AndAboveMalePercentOfTotalWb")
                .handler(this::extractDataWorldBankDemographicsPopulationAges65AndAboveMalePercentOfTotalWb);

        //This router permits to use an API to display the Population ages 65-69, male (% of male population)
        //from the URL : https://tradingeconomics.com/country-list/population-ages-65-69-male-percent-of-male-population-wb-data.html
        router.get("/api/TE/WorldBank/Demographics/PopulationAges65_69MalePercentOfMalePopulationWb")
                .handler(this::extractDataWorldBankDemographicsPopulationAges65_69MalePercentOfMalePopulationWb);

        //This router permits to use an API to display the Population ages 70-74, male (% of male population)
        //from the URL : https://tradingeconomics.com/country-list/population-ages-70-74-male-percent-of-male-population-wb-data.html
        router.get("/api/TE/WorldBank/Demographics/PopulationAges70_74MalePercentOfMalePopulationWb")
                .handler(this::extractDataWorldBankDemographicsPopulationAges70_74MalePercentOfMalePopulationWb);

        //This router permits to use an API to display the Population ages 75-79, male (% of male population)
        //from the URL : https://tradingeconomics.com/country-list/population-ages-75-79-male-percent-of-male-population-wb-data.html
        router.get("/api/TE/WorldBank/Demographics/PopulationAges75_79MalePercentOfMalePopulationWb")
                .handler(this::extractDataWorldBankDemographicsPopulationAges75_79MalePercentOfMalePopulationWb);

        //This router permits to use an API to display the Population ages 80 and above, female (% of female population)
        //from the URL : https://tradingeconomics.com/country-list/population-ages-80-and-above-female-percent-of-female-population-wb-data.html
        router.get("/api/TE/WorldBank/Demographics/PopulationAges80AndAboveFemalePercentOfFemalePopulationWb")
                .handler(this::extractDataWorldBankDemographicsPopulationAges80AndAboveFemalePercentOfFemalePopulationWb);

        //This router permits to use an API to display the Population census
        //from the URL : https://tradingeconomics.com/country-list/population-census-wb-data.html
        router.get("/api/TE/").handler(this::extractData);

        //This router permits to use an API to display the Population covered by mobile cellular network
        //from the URL : https://tradingeconomics.com/country-list/population-covered-by-mobile-cellular-network-percent-wb-data.html
        router.get("/api/TE/").handler(this::extractData);

        //This router permits to use an API to display the Population growth (annual %)
        //from the URL : https://tradingeconomics.com/country-list/population-growth-annual-percent-wb-data.html
        router.get("/api/TE/").handler(this::extractData);

        //This router permits to use an API to display the Population in extreme poor (<$1.25 a day) receiving 2 programs (%, preT)
        //from the URL : https://tradingeconomics.com/country-list/population-in-extreme-poor-%3C$1-25-a-day-receiving-2-programs-percent-pret-wb-data.html
        router.get("/api/TE/").handler(this::extractData);

        //This router permits to use an API to display the Population in extreme poor (<$1.25 a day) receiving 3 programs (%, preT)
        //from the URL : https://tradingeconomics.com/country-list/population-in-extreme-poor-%3C$1-25-a-day-receiving-3-programs-percent-pret-wb-data.html
        router.get("/api/TE/").handler(this::extractData);

        //This router permits to use an API to display the Population in extreme poor (<$1.25 a day) receiving 4 or more programs (%, preT)
        //from the URL : https://tradingeconomics.com/country-list/population-in-extreme-poor-%3C$1-25-a-day-receiving-4-or-more-programs-percent-pret-wb-data.html
        router.get("/api/TE/").handler(this::extractData);

        //This router permits to use an API to display the Population in extreme poor (<$1.25 a day) receiving only 1 program (%, preT)
        //from the URL : https://tradingeconomics.com/country-list/population-in-extreme-poor-%3C$1-25-a-day-receiving-only-1-program-percent-pret-wb-data.html
        router.get("/api/TE/").handler(this::extractData);

        //This router permits to use an API to display the Population in thousands, age 15+, female
        //from the URL : https://tradingeconomics.com/country-list/barro-lee-population-in-thousands-age-15-female-wb-data.html
        router.get("/api/TE/").handler(this::extractData);

        //This router permits to use an API to display the Population in thousands, age 15-19, female
        //from the URL : https://tradingeconomics.com/country-list/barro-lee-population-in-thousands-age-15-19-female-wb-data.html
        router.get("/api/TE/").handler(this::extractData);

        //This router permits to use an API to display the Population in thousands, age 20-24, female
        //from the URL : https://tradingeconomics.com/country-list/barro-lee-population-in-thousands-age-20-24-female-wb-data.html
        router.get("/api/TE/").handler(this::extractData);

        //This router permits to use an API to display the Population in thousands, age 25+, female
        //from the URL : https://tradingeconomics.com/country-list/barro-lee-population-in-thousands-age-25-female-wb-data.html
        router.get("/api/TE/").handler(this::extractData);

        //This router permits to use an API to display the Population in thousands, age 25-29, female
        //from the URL : https://tradingeconomics.com/country-list/barro-lee-population-in-thousands-age-25-29-female-wb-data.html
        router.get("/api/TE/").handler(this::extractData);

        //This router permits to use an API to display the Population in thousands, age 30-34, female
        //from the URL : https://tradingeconomics.com/country-list/barro-lee-population-in-thousands-age-30-34-female-wb-data.html
        router.get("/api/TE/").handler(this::extractData);

        //This router permits to use an API to display the Population in thousands, age 35-39, female
        //from the URL : https://tradingeconomics.com/country-list/barro-lee-population-in-thousands-age-35-39-female-wb-data.html
        router.get("/api/TE/").handler(this::extractData);

        //This router permits to use an API to display the Population in thousands, age 40-44, female
        //from the URL : https://tradingeconomics.com/country-list/barro-lee-population-in-thousands-age-40-44-female-wb-data.html
        router.get("/api/TE/").handler(this::extractData);

        //This router permits to use an API to display the Population in thousands, age 45-49, female
        //from the URL : https://tradingeconomics.com/country-list/barro-lee-population-in-thousands-age-45-49-female-wb-data.html
        router.get("/api/TE/").handler(this::extractData);

        //This router permits to use an API to display the Population in thousands, age 50-54, female
        //from the URL : https://tradingeconomics.com/country-list/barro-lee-population-in-thousands-age-50-54-female-wb-data.html
        router.get("/api/TE/").handler(this::extractData);

        //This router permits to use an API to display the Population in thousands, age 55-59, female
        //from the URL : https://tradingeconomics.com/country-list/barro-lee-population-in-thousands-age-55-59-female-wb-data.html
        router.get("/api/TE/").handler(this::extractData);

        //This router permits to use an API to display the Population in thousands, age 60-64, female
        //from the URL : https://tradingeconomics.com/country-list/barro-lee-population-in-thousands-age-60-64-female-wb-data.html
        router.get("/api/TE/").handler(this::extractData);

        //This router permits to use an API to display the Population in thousands, age 65-69, female
        //from the URL : https://tradingeconomics.com/country-list/barro-lee-population-in-thousands-age-65-69-female-wb-data.html
        router.get("/api/TE/").handler(this::extractData);

        //This router permits to use an API to display the Population in thousands, age 70-74, female
        //from the URL : https://tradingeconomics.com/country-list/barro-lee-population-in-thousands-age-70-74-female-wb-data.html
        router.get("/api/TE/").handler(this::extractData);

        //This router permits to use an API to display the Population in thousands, age 75+, female
        //from the URL : https://tradingeconomics.com/country-list/barro-lee-population-in-thousands-age-75-female-wb-data.html
        router.get("/api/TE/").handler(this::extractData);

        //This router permits to use an API to display the Population in urban agglomerations of more than 1 million
        //from the URL : https://tradingeconomics.com/country-list/population-in-urban-agglomerations-of-more-than-1-million-wb-data.html
        router.get("/api/TE/").handler(this::extractData);

        //This router permits to use an API to display the Population living in areas where elevation is below 5 meters
        //from the URL : https://tradingeconomics.com/country-list/population-living-in-areas-where-elevation-is-below-5-meters-percent-of-total-population-wb-data.html
        router.get("/api/TE/").handler(this::extractData);

        //This router permits to use an API to display the Population receiving 2 programs (%, preT)
        //from the URL : https://tradingeconomics.com/country-list/population-receiving-2-programs-percent-pret-wb-data.html
        router.get("/api/TE/").handler(this::extractData);

        //This router permits to use an API to display the Population receiving 2 programs -urban
        //from the URL : https://tradingeconomics.com/country-list/population-receiving-2-programs-urban-wb-data.html
        router.get("/api/TE/").handler(this::extractData);

        //This router permits to use an API to display the Population receiving 3 programs (%, preT)
        //from the URL : https://tradingeconomics.com/country-list/population-receiving-3-programs-percent-pret-wb-data.html
        router.get("/api/TE/").handler(this::extractData);

        //This router permits to use an API to display the Population receiving 3 programs -urban
        //from the URL : https://tradingeconomics.com/country-list/population-receiving-3-programs-urban-wb-data.html
        router.get("/api/TE/").handler(this::extractData);

        //This router permits to use an API to display the Population receiving 4 or more programs (%, preT)
        //from the URL : https://tradingeconomics.com/country-list/population-receiving-4-or-more-programs-percent-pret-wb-data.html
        router.get("/api/TE/").handler(this::extractData);

        //This router permits to use an API to display the Population receiving 4 or more programs -urban
        //from the URL : https://tradingeconomics.com/country-list/population-receiving-4-or-more-programs-urban-wb-data.html
        router.get("/api/TE/").handler(this::extractData);

        //This router permits to use an API to display the Population receiving only 1 program (%, preT)
        //from the URL : https://tradingeconomics.com/country-list/population-receiving-only-1-program-percent-pret-wb-data.html
        router.get("/api/TE/").handler(this::extractData);

        //This router permits to use an API to display the Population receiving only 1 program -urban
        //from the URL : https://tradingeconomics.com/country-list/population-receiving-only-1-program-urban-wb-data.html
        router.get("/api/TE/").handler(this::extractData);

        //This router permits to use an API to display the Population, age 0, male
        //from the URL : https://tradingeconomics.com/country-list/population-age-0-male-wb-data.html
        router.get("/api/TE/").handler(this::extractData);

        //This router permits to use an API to display the Population, age 1, female
        //from the URL : https://tradingeconomics.com/country-list/population-age-1-female-wb-data.html
        router.get("/api/TE/").handler(this::extractData);

        //This router permits to use an API to display the Population, age 1, total
        //from the URL : https://tradingeconomics.com/country-list/population-age-1-total-wb-data.html
        router.get("/api/TE/").handler(this::extractData);

        //This router permits to use an API to display the Population, age 10, male
        //from the URL : https://tradingeconomics.com/country-list/population-age-10-male-wb-data.html
        router.get("/api/TE/").handler(this::extractData);

        //This router permits to use an API to display the Population, age 11, female
        //from the URL : https://tradingeconomics.com/country-list/population-age-11-female-wb-data.html
        router.get("/api/TE/").handler(this::extractData);

        //This router permits to use an API to display the Population, age 11, total
        //from the URL : https://tradingeconomics.com/country-list/population-age-11-total-wb-data.html
        router.get("/api/TE/").handler(this::extractData);

        //This router permits to use an API to display the Population, age 12, male
        //from the URL : https://tradingeconomics.com/country-list/population-age-12-male-wb-data.html
        router.get("/api/TE/").handler(this::extractData);

        //This router permits to use an API to display the Population, age 13, female
        //from the URL : https://tradingeconomics.com/country-list/population-age-13-female-wb-data.html
        router.get("/api/TE/").handler(this::extractData);

        //This router permits to use an API to display the Population, age 13, total
        //from the URL : https://tradingeconomics.com/country-list/population-age-13-total-wb-data.html
        router.get("/api/TE/").handler(this::extractData);

        //This router permits to use an API to display the Population, age 14, male
        //from the URL : https://tradingeconomics.com/country-list/population-age-14-male-wb-data.html
        router.get("/api/TE/").handler(this::extractData);

        //This router permits to use an API to display the Population, age 15, female
        //from the URL : https://tradingeconomics.com/country-list/population-age-15-female-wb-data.html
        router.get("/api/TE/").handler(this::extractData);

        //This router permits to use an API to display the Population, age 15, total
        //from the URL : https://tradingeconomics.com/country-list/population-age-15-total-wb-data.html
        router.get("/api/TE/").handler(this::extractData);

        //This router permits to use an API to display the Population, age 16, male
        //from the URL : https://tradingeconomics.com/country-list/population-age-16-male-wb-data.html
        router.get("/api/TE/").handler(this::extractData);

        //This router permits to use an API to display the Population, age 17, female
        //from the URL : https://tradingeconomics.com/country-list/population-age-17-female-wb-data.html
        router.get("/api/TE/").handler(this::extractData);

        //This router permits to use an API to display the Population, age 17, total
        //from the URL : https://tradingeconomics.com/country-list/population-age-17-total-wb-data.html
        router.get("/api/TE/").handler(this::extractData);

        //This router permits to use an API to display the Population, age 18, male
        //from the URL : https://tradingeconomics.com/country-list/population-age-18-male-wb-data.html
        router.get("/api/TE/").handler(this::extractData);

        //This router permits to use an API to display the Population, age 19, female
        //from the URL : https://tradingeconomics.com/country-list/population-age-19-female-wb-data.html
        router.get("/api/TE/").handler(this::extractData);

        //This router permits to use an API to display the Population, age 19, total
        //from the URL : https://tradingeconomics.com/country-list/population-age-19-total-wb-data.html
        router.get("/api/TE/").handler(this::extractData);

        //This router permits to use an API to display the Population, age 2, male
        //from the URL : https://tradingeconomics.com/country-list/population-age-2-male-wb-data.html
        router.get("/api/TE/").handler(this::extractData);

        //This router permits to use an API to display the Population, age 20, female
        //from the URL : https://tradingeconomics.com/country-list/population-age-20-female-wb-data.html
        router.get("/api/TE/").handler(this::extractData);

        //This router permits to use an API to display the Population, age 20, total
        //from the URL : https://tradingeconomics.com/country-list/population-age-20-total-wb-data.html
        router.get("/api/TE/").handler(this::extractData);

        //This router permits to use an API to display the Population, age 21, male
        //from the URL : https://tradingeconomics.com/country-list/population-age-21-male-wb-data.html
        router.get("/api/TE/").handler(this::extractData);

        //This router permits to use an API to display the Population, age 22, female
        //from the URL : https://tradingeconomics.com/country-list/population-age-22-female-wb-data.html
        router.get("/api/TE/").handler(this::extractData);

        //This router permits to use an API to display the Population, age 22, total
        //from the URL : https://tradingeconomics.com/country-list/population-age-22-total-wb-data.html
        router.get("/api/TE/").handler(this::extractData);

        //This router permits to use an API to display the Population, age 23, male
        //from the URL : https://tradingeconomics.com/country-list/population-age-23-male-wb-data.html
        router.get("/api/TE/").handler(this::extractData);

        //This router permits to use an API to display the Population, age 24, female
        //from the URL : https://tradingeconomics.com/country-list/population-age-24-female-wb-data.html
        router.get("/api/TE/").handler(this::extractData);

        //This router permits to use an API to display the Population, age 24, total
        //from the URL : https://tradingeconomics.com/country-list/population-age-24-total-wb-data.html
        router.get("/api/TE/").handler(this::extractData);

        //This router permits to use an API to display the Population, age 25, male
        //from the URL : https://tradingeconomics.com/country-list/population-age-25-male-wb-data.html
        router.get("/api/TE/").handler(this::extractData);

        //This router permits to use an API to display the Population, age 3, female
        //from the URL : https://tradingeconomics.com/country-list/population-age-3-female-wb-data.html
        router.get("/api/TE/").handler(this::extractData);

        //This router permits to use an API to display the Population, age 3, total
        //from the URL : https://tradingeconomics.com/country-list/population-age-3-total-wb-data.html
        router.get("/api/TE/").handler(this::extractData);

        //This router permits to use an API to display the Population, age 4, male
        //from the URL : https://tradingeconomics.com/country-list/population-age-4-male-wb-data.html
        router.get("/api/TE/").handler(this::extractData);

        //This router permits to use an API to display the Population, age 5, female
        //from the URL : https://tradingeconomics.com/country-list/population-age-5-female-wb-data.html
        router.get("/api/TE/").handler(this::extractData);

        //This router permits to use an API to display the Population, age 5, total
        //from the URL : https://tradingeconomics.com/country-list/population-age-5-total-wb-data.html
        router.get("/api/TE/").handler(this::extractData);

        //This router permits to use an API to display the Population, age 6, male
        //from the URL : https://tradingeconomics.com/country-list/population-age-6-male-wb-data.html
        router.get("/api/TE/").handler(this::extractData);

        //This router permits to use an API to display the Population, age 7, female
        //from the URL : https://tradingeconomics.com/country-list/population-age-7-female-wb-data.html
        router.get("/api/TE/").handler(this::extractData);

        //This router permits to use an API to display the Population, age 7, total
        //from the URL : https://tradingeconomics.com/country-list/population-age-7-total-wb-data.html
        router.get("/api/TE/").handler(this::extractData);

        //This router permits to use an API to display the Population, age 8, male
        //from the URL : https://tradingeconomics.com/country-list/population-age-8-male-wb-data.html
        router.get("/api/TE/").handler(this::extractData);

        //This router permits to use an API to display the Population, age 9, female
        //from the URL : https://tradingeconomics.com/country-list/population-age-9-female-wb-data.html
        router.get("/api/TE/").handler(this::extractData);

        //This router permits to use an API to display the Population, age 9, total
        //from the URL : https://tradingeconomics.com/country-list/population-age-9-total-wb-data.html
        router.get("/api/TE/").handler(this::extractData);

        //This router permits to use an API to display the Population, ages 0-14, total
        //from the URL : https://tradingeconomics.com/country-list/population-ages-0-14-total-wb-data.html
        router.get("/api/TE/").handler(this::extractData);

        //This router permits to use an API to display the Population, ages 10-14, male
        //from the URL : https://tradingeconomics.com/country-list/population-ages-10-14-male-wb-data.html
        router.get("/api/TE/").handler(this::extractData);

        //This router permits to use an API to display the Population, ages 10-15, female
        //from the URL : https://tradingeconomics.com/country-list/population-ages-10-15-female-wb-data.html
        router.get("/api/TE/").handler(this::extractData);

        //This router permits to use an API to display the Population, ages 10-15, total
        //from the URL : https://tradingeconomics.com/country-list/population-ages-10-15-total-wb-data.html
        router.get("/api/TE/").handler(this::extractData);

        //This router permits to use an API to display the Population, ages 10-16, male
        //from the URL : https://tradingeconomics.com/country-list/population-ages-10-16-male-wb-data.html
        router.get("/api/TE/").handler(this::extractData);

        //This router permits to use an API to display the Population, ages 10-17, female
        //from the URL : https://tradingeconomics.com/country-list/population-ages-10-17-female-wb-data.html
        router.get("/api/TE/").handler(this::extractData);

        //This router permits to use an API to display the Population, ages 10-17, total
        //from the URL : https://tradingeconomics.com/country-list/population-ages-10-17-total-wb-data.html
        router.get("/api/TE/").handler(this::extractData);

        //This router permits to use an API to display the Population, ages 10-18, male
        //from the URL : https://tradingeconomics.com/country-list/population-ages-10-18-male-wb-data.html
        router.get("/api/TE/").handler(this::extractData);

        //This router permits to use an API to display the Population, ages 11-15, female
        //from the URL : https://tradingeconomics.com/country-list/population-ages-11-15-female-wb-data.html
        router.get("/api/TE/").handler(this::extractData);

        //This router permits to use an API to display the Population, ages 11-15, total
        //from the URL : https://tradingeconomics.com/country-list/population-ages-11-15-total-wb-data.html
        router.get("/api/TE/").handler(this::extractData);

        //This router permits to use an API to display the Population, ages 11-16, male
        //from the URL : https://tradingeconomics.com/country-list/population-ages-11-16-male-wb-data.html
        router.get("/api/TE/").handler(this::extractData);

        //This router permits to use an API to display the Population, ages 11-17, female
        //from the URL : https://tradingeconomics.com/country-list/population-ages-11-17-female-wb-data.html
        router.get("/api/TE/").handler(this::extractData);

        //This router permits to use an API to display the Population, ages 11-17, total
        //from the URL : https://tradingeconomics.com/country-list/population-ages-11-17-total-wb-data.html
        router.get("/api/TE/").handler(this::extractData);

        //This router permits to use an API to display the Population, ages 11-18, male
        //from the URL : https://tradingeconomics.com/country-list/population-ages-11-18-male-wb-data.html
        router.get("/api/TE/").handler(this::extractData);

        //This router permits to use an API to display the Population, ages 12-15, female
        //from the URL : https://tradingeconomics.com/country-list/population-ages-12-15-female-wb-data.html
        router.get("/api/TE/").handler(this::extractData);

        //This router permits to use an API to display the Population, ages 12-15, total
        //from the URL : https://tradingeconomics.com/country-list/population-ages-12-15-total-wb-data.html
        router.get("/api/TE/").handler(this::extractData);

        //This router permits to use an API to display the Population, ages 12-16, male
        //from the URL : https://tradingeconomics.com/country-list/population-ages-12-16-male-wb-data.html
        router.get("/api/TE/").handler(this::extractData);

        //This router permits to use an API to display the Population, ages 12-17, female
        //from the URL : https://tradingeconomics.com/country-list/population-ages-12-17-female-wb-data.html
        router.get("/api/TE/").handler(this::extractData);

        //This router permits to use an API to display the Population, ages 12-17, total
        //from the URL : https://tradingeconomics.com/country-list/population-ages-12-17-total-wb-data.html
        router.get("/api/TE/").handler(this::extractData);

        //This router permits to use an API to display the Population, ages 12-18, male
        //from the URL : https://tradingeconomics.com/country-list/population-ages-12-18-male-wb-data.html
        router.get("/api/TE/").handler(this::extractData);

        //This router permits to use an API to display the Population, ages 13-16, female
        //from the URL : https://tradingeconomics.com/country-list/population-ages-13-16-female-wb-data.html
        router.get("/api/TE/").handler(this::extractData);

        //This router permits to use an API to display the Population, ages 13-16, total
        //from the URL : https://tradingeconomics.com/country-list/population-ages-13-16-total-wb-data.html
        router.get("/api/TE/").handler(this::extractData);

        //This router permits to use an API to display the Population, ages 13-17, male
        //from the URL : https://tradingeconomics.com/country-list/population-ages-13-17-male-wb-data.html
        router.get("/api/TE/").handler(this::extractData);

        //This router permits to use an API to display the Population, ages 13-18, female
        //from the URL : https://tradingeconomics.com/country-list/population-ages-13-18-female-wb-data.html
        router.get("/api/TE/").handler(this::extractData);

        //This router permits to use an API to display the Population, ages 13-18, total
        //from the URL : https://tradingeconomics.com/country-list/population-ages-13-18-total-wb-data.html
        router.get("/api/TE/").handler(this::extractData);

        //This router permits to use an API to display the Population, ages 13-19, male
        //from the URL : https://tradingeconomics.com/country-list/population-ages-13-19-male-wb-data.html
        router.get("/api/TE/").handler(this::extractData);

        //This router permits to use an API to display the Population, ages 14-18, female
        //from the URL : https://tradingeconomics.com/country-list/population-ages-14-18-female-wb-data.html
        router.get("/api/TE/").handler(this::extractData);

        //This router permits to use an API to display the Population, ages 14-18, total
        //from the URL : https://tradingeconomics.com/country-list/population-ages-14-18-total-wb-data.html
        router.get("/api/TE/").handler(this::extractData);

        //This router permits to use an API to display the Population, ages 14-19, male
        //from the URL : https://tradingeconomics.com/country-list/population-ages-14-19-male-wb-data.html
        router.get("/api/TE/").handler(this::extractData);

        //This router permits to use an API to display the Population, ages 15-24, female
        //from the URL : https://tradingeconomics.com/country-list/population-ages-15-24-female-wb-data.html
        router.get("/api/TE/").handler(this::extractData);

        //This router permits to use an API to display the Population, ages 15-24, total
        //from the URL : https://tradingeconomics.com/country-list/population-ages-15-24-total-wb-data.html
        router.get("/api/TE/").handler(this::extractData);

        //This router permits to use an API to display the Population, ages 3-5, male
        //from the URL : https://tradingeconomics.com/country-list/population-ages-3-5-male-wb-data.html
        router.get("/api/TE/").handler(this::extractData);

        //This router permits to use an API to display the Population, ages 4-6, female
        //from the URL : https://tradingeconomics.com/country-list/population-ages-4-6-female-wb-data.html
        router.get("/api/TE/").handler(this::extractData);

        //This router permits to use an API to display the Population, ages 4-6, total
        //from the URL : https://tradingeconomics.com/country-list/population-ages-4-6-total-wb-data.html
        router.get("/api/TE/").handler(this::extractData);

        //This router permits to use an API to display the Population, ages 5-10, male
        //from the URL : https://tradingeconomics.com/country-list/population-ages-5-10-male-wb-data.html
        router.get("/api/TE/").handler(this::extractData);

        //This router permits to use an API to display the Population, ages 5-11, female
        //from the URL : https://tradingeconomics.com/country-list/population-ages-5-11-female-wb-data.html
        router.get("/api/TE/").handler(this::extractData);

        //This router permits to use an API to display the Population, ages 5-11, total
        //from the URL : https://tradingeconomics.com/country-list/population-ages-5-11-total-wb-data.html
        router.get("/api/TE/").handler(this::extractData);

        //This router permits to use an API to display the Population, ages 5-9, male
        //from the URL : https://tradingeconomics.com/country-list/population-ages-5-9-male-wb-data.html
        router.get("/api/TE/").handler(this::extractData);

        //This router permits to use an API to display the Population, ages 6-10, female
        //from the URL : https://tradingeconomics.com/country-list/population-ages-6-10-female-wb-data.html
        router.get("/api/TE/").handler(this::extractData);

        //This router permits to use an API to display the Population, ages 6-10, total
        //from the URL : https://tradingeconomics.com/country-list/population-ages-6-10-total-wb-data.html
        router.get("/api/TE/").handler(this::extractData);

        //This router permits to use an API to display the Population, ages 6-11, male
        //from the URL : https://tradingeconomics.com/country-list/population-ages-6-11-male-wb-data.html
        router.get("/api/TE/").handler(this::extractData);

        //This router permits to use an API to display the Population, ages 6-12, female
        //from the URL : https://tradingeconomics.com/country-list/population-ages-6-12-female-wb-data.html
        router.get("/api/TE/").handler(this::extractData);

        //This router permits to use an API to display the Population, ages 6-12, total
        //from the URL : https://tradingeconomics.com/country-list/population-ages-6-12-total-wb-data.html
        router.get("/api/TE/").handler(this::extractData);

        //This router permits to use an API to display the Population, ages 6-9, male
        //from the URL : https://tradingeconomics.com/country-list/population-ages-6-9-male-wb-data.html
        router.get("/api/TE/").handler(this::extractData);

        //This router permits to use an API to display the Population, ages 7-10, female
        //from the URL : https://tradingeconomics.com/country-list/population-ages-7-10-female-wb-data.html
        router.get("/api/TE/").handler(this::extractData);

        //This router permits to use an API to display the Population, ages 7-10, total
        //from the URL : https://tradingeconomics.com/country-list/population-ages-7-10-total-wb-data.html
        router.get("/api/TE/").handler(this::extractData);

        //This router permits to use an API to display the Population, ages 7-11, male
        //from the URL : https://tradingeconomics.com/country-list/population-ages-7-11-male-wb-data.html
        router.get("/api/TE/").handler(this::extractData);

        //This router permits to use an API to display the Population, ages 7-12, female
        //from the URL : https://tradingeconomics.com/country-list/population-ages-7-12-female-wb-data.html
        router.get("/api/TE/").handler(this::extractData);

        //This router permits to use an API to display the Population, ages 7-12, total
        //from the URL : https://tradingeconomics.com/country-list/population-ages-7-12-total-wb-data.html
        router.get("/api/TE/").handler(this::extractData);

        //This router permits to use an API to display the Population, ages 7-13, male
        //from the URL : https://tradingeconomics.com/country-list/population-ages-7-13-male-wb-data.html
        router.get("/api/TE/").handler(this::extractData);

        //This router permits to use an API to display the Population, ages 7-9, female
        //from the URL : https://tradingeconomics.com/country-list/population-ages-7-9-female-wb-data.html
        router.get("/api/TE/").handler(this::extractData);

        //This router permits to use an API to display the Population, ages 7-9, total
        //from the URL : https://tradingeconomics.com/country-list/population-ages-7-9-total-wb-data.html
        router.get("/api/TE/").handler(this::extractData);

        //This router permits to use an API to display the Population, female (% of total)
        //from the URL : https://tradingeconomics.com/country-list/population-female-percent-of-total-wb-data.html
        router.get("/api/TE/").handler(this::extractData);

        //This router permits to use an API to display the Population, male (% of total)
        //from the URL : https://tradingeconomics.com/country-list/population-male-percent-of-total-wb-data.html
        router.get("/api/TE/").handler(this::extractData);

        //This router permits to use an API to display the Poverty headcount ratio at $1.25 a day (PPP) (% of population)
        //from the URL : https://tradingeconomics.com/country-list/poverty-headcount-ratio-at-dollar1-25-a-day-ppp-percent-of-population-wb-data.html
        router.get("/api/TE/").handler(this::extractData);

        //This router permits to use an API to display the Poverty headcount ratio at $2.5 a day (PPP) (% of population)
        //from the URL : https://tradingeconomics.com/country-list/poverty-headcount-ratio-at-dollar2-5-a-day-ppp-percent-of-population-wb-data.html
        router.get("/api/TE/").handler(this::extractData);

        //This router permits to use an API to display the Poverty headcount ratio at $5 a day (PPP) (% of population)
        //from the URL : https://tradingeconomics.com/country-list/poverty-headcount-ratio-at-$5-a-day-ppp-percent-of-population-wb-data.html
        router.get("/api/TE/").handler(this::extractData);

        //This router permits to use an API to display the Poverty headcount ratio at rural poverty line (% of rural population)
        //from the URL : https://tradingeconomics.com/country-list/poverty-headcount-ratio-at-rural-poverty-line-percent-of-rural-population-wb-data.html
        router.get("/api/TE/").handler(this::extractData);

        //This router permits to use an API to display the Prevalence of obesity, female (% of female population ages 18+)
        //from the URL : https://tradingeconomics.com/country-list/prevalence-of-obesity-female-percent-of-female-population-ages-18-wb-data.html
        router.get("/api/TE/").handler(this::extractData);

        //This router permits to use an API to display the Prevalence of undernourishment (% of population)
        //from the URL : https://tradingeconomics.com/country-list/prevalence-of-undernourishment-percent-of-population-wb-data.html
        router.get("/api/TE/").handler(this::extractData);

        //This router permits to use an API to display the Refugee population by country or territory of asylum
        //from the URL : https://tradingeconomics.com/country-list/refugee-population-by-country-or-territory-of-asylum-wb-data.html
        router.get("/api/TE/").handler(this::extractData);

        //This router permits to use an API to display the Rural population
        //from the URL : https://tradingeconomics.com/country-list/rural-population-wb-data.html
        router.get("/api/TE/").handler(this::extractData);

        //This router permits to use an API to display the Rural population density (rural population per sq. km of arable land)
        //from the URL : https://tradingeconomics.com/country-list/rural-population-density-rural-population-per-sq-km-of-arable-land-wb-data.html
        router.get("/api/TE/").handler(this::extractData);

        //This router permits to use an API to display the Rural population, female (% of total)
        //from the URL : https://tradingeconomics.com/country-list/rural-population-female-percent-of-total-wb-data.html
        router.get("/api/TE/").handler(this::extractData);

        //This router permits to use an API to display the Share of children (0-14) in total population
        //from the URL : https://tradingeconomics.com/country-list/share-of-children-0-14-in-total-population-wb-data.html
        router.get("/api/TE/").handler(this::extractData);

        //This router permits to use an API to display the Share of children (0-14) in total population - male
        //from the URL : https://tradingeconomics.com/country-list/share-of-children-0-14-in-total-population-male-wb-data.html
        router.get("/api/TE/").handler(this::extractData);

        //This router permits to use an API to display the Share of children (0-14) in total population - urban
        //from the URL : https://tradingeconomics.com/country-list/share-of-children-0-14-in-total-population-urban-wb-data.html
        router.get("/api/TE/").handler(this::extractData);

        //This router permits to use an API to display the Share of elderly (60+) in total population - female
        //from the URL : https://tradingeconomics.com/country-list/share-of-elderly-60-in-total-population-female-wb-data.html
        router.get("/api/TE/").handler(this::extractData);

        //This router permits to use an API to display the Share of elderly (60+) in total population - rural
        //from the URL : https://tradingeconomics.com/country-list/share-of-elderly-60-in-total-population-rural-wb-data.html
        router.get("/api/TE/").handler(this::extractData);

        //This router permits to use an API to display the Share of employed in agriculture -total population
        //from the URL : https://tradingeconomics.com/country-list/share-of-employed-in-agriculture-total-population-wb-data.html
        router.get("/api/TE/").handler(this::extractData);

        //This router permits to use an API to display the Share of employed in services -total population
        //from the URL : https://tradingeconomics.com/country-list/share-of-employed-in-services-total-population-wb-data.html
        router.get("/api/TE/").handler(this::extractData);

        //This router permits to use an API to display the Share of employed workers who are employers in total population
        //from the URL : https://tradingeconomics.com/country-list/share-of-employed-workers-who-are-employers-in-total-population-wb-data.html
        router.get("/api/TE/").handler(this::extractData);

        //This router permits to use an API to display the Share of employed workers who are unpaid in total population
        //from the URL : https://tradingeconomics.com/country-list/share-of-employed-workers-who-are-unpaid-in-total-population-wb-data.html
        router.get("/api/TE/").handler(this::extractData);

        //This router permits to use an API to display the Share of households with children in total population
        //from the URL : https://tradingeconomics.com/country-list/share-of-households-with-children-in-total-population-wb-data.html
        router.get("/api/TE/").handler(this::extractData);

        //This router permits to use an API to display the Share of households with working age adults in total population
        //from the URL : https://tradingeconomics.com/country-list/share-of-households-with-working-age-adults-in-total-population-wb-data.html
        router.get("/api/TE/").handler(this::extractData);

        //This router permits to use an API to display the Share of inactive students in total population
        //from the URL : https://tradingeconomics.com/country-list/share-of-inactive-students-in-total-population-wb-data.html
        router.get("/api/TE/").handler(this::extractData);

        //This router permits to use an API to display the Share of working age (25-59) in total population
        //from the URL : https://tradingeconomics.com/country-list/share-of-working-age-25-59-in-total-population-wb-data.html
        router.get("/api/TE/").handler(this::extractData);

        //This router permits to use an API to display the Share of working age (25-59) in total population - male
        //from the URL : https://tradingeconomics.com/country-list/share-of-working-age-25-59-in-total-population-male-wb-data.html
        router.get("/api/TE/").handler(this::extractData);

        //This router permits to use an API to display the Share of working age (25-59) in total population - urban
        //from the URL : https://tradingeconomics.com/country-list/share-of-working-age-25-59-in-total-population-urban-wb-data.html
        router.get("/api/TE/").handler(this::extractData);

        //This router permits to use an API to display the Share of youth (15-24) in total population - female
        //from the URL : https://tradingeconomics.com/country-list/share-of-youth-15-24-in-total-population-female-wb-data.html
        router.get("/api/TE/").handler(this::extractData);

        //This router permits to use an API to display the Share of youth (15-24) in total population - rural
        //from the URL : https://tradingeconomics.com/country-list/share-of-youth-15-24-in-total-population-rural-wb-data.html
        router.get("/api/TE/").handler(this::extractData);

        //This router permits to use an API to display the Specialist surgical workforce (per 100,000 population)
        //from the URL : https://tradingeconomics.com/country-list/specialist-surgical-workforce-per-100-000-population-wb-data.html
        router.get("/api/TE/").handler(this::extractData);

        //This router permits to use an API to display the Survey mean consumption or income per capita, bottom 40% of population (2005 PPP $ per day)
        //from the URL : https://tradingeconomics.com/country-list/survey-mean-consumption-or-income-per-capita-bottom-40percent-of-population-2005-ppp-dollar-per-day-wb-data.html
        router.get("/api/TE/").handler(this::extractData);

        //This router permits to use an API to display the Survey mean consumption or income per capita, total population (2005 PPP $ per day)
        //from the URL : https://tradingeconomics.com/country-list/survey-mean-consumption-or-income-per-capita-total-population-2005-ppp-dollar-per-day-wb-data.html
        router.get("/api/TE/").handler(this::extractData);

        //This router permits to use an API to display the Total Population for Age 65 and above (only 2005 and 2010) (in number of people)
        //from the URL : https://tradingeconomics.com/country-list/total-population-for-age-65-and-above-only-2005-and-2010-in-number-of-people-wb-data.html
        router.get("/api/TE/").handler(this::extractData);

        //This router permits to use an API to display the Tuberculosis prevalence rate, low uncertainty bound (per 1000,000 population, WHO)
        //from the URL : https://tradingeconomics.com/country-list/tuberculosis-prevalence-rate-low-uncertainty-bound-per-1000000-population-who-wb-data.html
        router.get("/api/TE/").handler(this::extractData);

        //This router permits to use an API to display the Urban population (% of total)
        //from the URL : https://tradingeconomics.com/country-list/urban-population-percent-of-total-wb-data.html
        router.get("/api/TE/").handler(this::extractData);

        //This router permits to use an API to display the Urban population living in areas where elevation is below 5 meters
        //from the URL : https://tradingeconomics.com/country-list/urban-population-living-in-areas-where-elevation-is-below-5-meters-wb-data.html
        router.get("/api/TE/").handler(this::extractData);

        //This router permits to use an API to display the Use of insecticide-treated bed nets (% of under-5 population)
        //from the URL : https://tradingeconomics.com/country-list/use-of-insecticide-treated-bed-nets-percent-of-under-5-population-wb-data.html
        router.get("/api/TE/").handler(this::extractData);

        //This router permits to use an API to display the Access to a mobile phone or internet at home, female (% age 15+)
        //from the URL : https://tradingeconomics.com/country-list/access-to-a-mobile-phone-or-internet-at-home-female-percent-age-15-wb-data.html
        router.get("/api/TE/").handler(this::extractData);

        //This router permits to use an API to display the Access to a mobile phone or internet at home, income, richest 60% (% age 15+)
        //from the URL : https://tradingeconomics.com/country-list/access-to-a-mobile-phone-or-internet-at-home-income-richest-60percent-percent-age-15-wb-data.html
        router.get("/api/TE/").handler(this::extractData);

        //This router permits to use an API to display the Access to a mobile phone or internet at home, older adults (% age 35+)
        //from the URL : https://tradingeconomics.com/country-list/access-to-a-mobile-phone-or-internet-at-home-older-adults-percent-age-35-wb-data.html
        router.get("/api/TE/").handler(this::extractData);

        //This router permits to use an API to display the Access to an all-season road (% of rural population)
        //from the URL : https://tradingeconomics.com/country-list/access-to-an-all-season-road-percent-of-rural-population-wb-data.html
        router.get("/api/TE/").handler(this::extractData);

        //This router permits to use an API to display the Access to an improved water source , rural (% of rural population): Q5 (highest)
        //from the URL : https://tradingeconomics.com/country-list/access-to-an-improved-water-source-rural-percent-of-rural-population-q5-highest-wb-data.html
        router.get("/api/TE/").handler(this::extractData);

        //This router permits to use an API to display the Access to an improved water source, rural (% of rural population): Q2
        //from the URL : https://tradingeconomics.com/country-list/access-to-an-improved-water-source-rural-percent-of-rural-population-q2-wb-data.html
        router.get("/api/TE/").handler(this::extractData);

        //This router permits to use an API to display the Access to an improved water source, rural (% of rural population): Q4
        //from the URL : https://tradingeconomics.com/country-list/access-to-an-improved-water-source-rural-percent-of-rural-population-q4-wb-data.html
        router.get("/api/TE/").handler(this::extractData);

        //This router permits to use an API to display the Access to an improved water source, urban : Q2
        //from the URL : https://tradingeconomics.com/country-list/access-to-an-improved-water-source-urban-q2-wb-data.html
        router.get("/api/TE/").handler(this::extractData);

        //This router permits to use an API to display the Access to an improved water source, urban : Q4
        //from the URL : https://tradingeconomics.com/country-list/access-to-an-improved-water-source-urban-q4-wb-data.html
        router.get("/api/TE/").handler(this::extractData);

        //This router permits to use an API to display the Access to clean fuels and technologies for cooking (% of population)
        //from the URL : https://tradingeconomics.com/country-list/access-to-clean-fuels-and-technologies-for-cooking-percent-of-population-wb-data.html
        router.get("/api/TE/").handler(this::extractData);

        //This router permits to use an API to display the Access to electricity
        //from the URL : https://tradingeconomics.com/country-list/access-to-electricity-percent-of-urban-population-wb-data.html
        router.get("/api/TE/").handler(this::extractData);

        //This router permits to use an API to display the Access to electricity (% of rural population)
        //from the URL : https://tradingeconomics.com/country-list/access-to-electricity-percent-of-rural-population-wb-data.html
        router.get("/api/TE/").handler(this::extractData);

        //This router permits to use an API to display the Access to electricity, urban
        //from the URL : https://tradingeconomics.com/country-list/access-to-electricity-urban-wb-data.html
        router.get("/api/TE/").handler(this::extractData);

        //This router permits to use an API to display the Access to improved sanitation facilities, rural (% of rural population): Q1 (lowest)
        //from the URL : https://tradingeconomics.com/country-list/access-to-improved-sanitation-facilities-rural-percent-of-rural-population-q1-lowest-wb-data.html
        router.get("/api/TE/").handler(this::extractData);

        //This router permits to use an API to display the Access to improved sanitation facilities, rural (% of rural population): Q3
        //from the URL : https://tradingeconomics.com/country-list/access-to-improved-sanitation-facilities-rural-percent-of-rural-population-q3-wb-data.html
        router.get("/api/TE/").handler(this::extractData);

        //This router permits to use an API to display the Access to improved sanitation facilities, rural (% of rural population): Q5 (highest)
        //from the URL : https://tradingeconomics.com/country-list/access-to-improved-sanitation-facilities-rural-percent-of-rural-population-q5-highest-wb-data.html
        router.get("/api/TE/").handler(this::extractData);

        //This router permits to use an API to display the Access to improved sanitation facilities, urban : Q2
        //from the URL : https://tradingeconomics.com/country-list/access-to-improved-sanitation-facilities-urban-q2-wb-data.html
        router.get("/api/TE/").handler(this::extractData);

        //This router permits to use an API to display the Access to improved sanitation facilities, urban : Q3
        //from the URL : https://tradingeconomics.com/country-list/access-to-improved-sanitation-facilities-urban-q3-wb-data.html
        router.get("/api/TE/").handler(this::extractData);

        //This router permits to use an API to display the Access to improved sanitation facilities, urban : QT (quintile total)
        //from the URL : https://tradingeconomics.com/country-list/access-to-improved-sanitation-facilities-urban-qt-quintile-total-wb-data.html
        router.get("/api/TE/").handler(this::extractData);

        //This router permits to use an API to display the Access to Non-Solid Fuel
        //from the URL : https://tradingeconomics.com/country-list/access-to-non-solid-fuel-percent-of-total-population-wb-data.html
        router.get("/api/TE/").handler(this::extractData);

        //This router permits to use an API to display the Access to Non-Solid Fuel Urban Population
        //from the URL : https://tradingeconomics.com/country-list/access-to-non-solid-fuel-percent-of-urban-population-wb-data.html
        router.get("/api/TE/").handler(this::extractData);

        //This router permits to use an API to display the Access to water
        //from the URL : https://tradingeconomics.com/country-list/access-to-water-wb-data.html
        router.get("/api/TE/").handler(this::extractData);

        //This router permits to use an API to display the Age dependency ratio, old (% of working-age population)
        //from the URL : https://tradingeconomics.com/country-list/age-dependency-ratio-old-percent-of-working-age-population-wb-data.html
        router.get("/api/TE/").handler(this::extractData);

        //This router permits to use an API to display the Age population, age 06, female, interpolated
        //from the URL : https://tradingeconomics.com/country-list/age-population-age-06-female-interpolated-wb-data.html
        router.get("/api/TE/").handler(this::extractData);

        //This router permits to use an API to display the Age population, age 06, male, interpolated
        //from the URL : https://tradingeconomics.com/country-list/age-population-age-06-male-interpolated-wb-data.html
        router.get("/api/TE/").handler(this::extractData);

        //This router permits to use an API to display the Age population, age 07, male, interpolated
        //from the URL : https://tradingeconomics.com/country-list/age-population-age-07-male-interpolated-wb-data.html
        router.get("/api/TE/").handler(this::extractData);

        //This router permits to use an API to display the Age population, age 08, male, interpolated
        //from the URL : https://tradingeconomics.com/country-list/age-population-age-08-male-interpolated-wb-data.html
        router.get("/api/TE/").handler(this::extractData);

        //This router permits to use an API to display the Age population, age 09, male, interpolated
        //from the URL : https://tradingeconomics.com/country-list/age-population-age-09-male-interpolated-wb-data.html
        router.get("/api/TE/").handler(this::extractData);

        //This router permits to use an API to display the Age population, age 10, male
        //from the URL : https://tradingeconomics.com/country-list/age-population-age-10-male-wb-data.html
        router.get("/api/TE/").handler(this::extractData);

        //This router permits to use an API to display the Age population, age 11, male
        //from the URL : https://tradingeconomics.com/country-list/age-population-age-11-male-wb-data.html
        router.get("/api/TE/").handler(this::extractData);

        //This router permits to use an API to display the Age population, age 12, male
        //from the URL : https://tradingeconomics.com/country-list/age-population-age-12-male-wb-data.html
        router.get("/api/TE/").handler(this::extractData);

        //This router permits to use an API to display the Age population, age 13, male
        //from the URL : https://tradingeconomics.com/country-list/age-population-age-13-male-wb-data.html
        router.get("/api/TE/").handler(this::extractData);

        //This router permits to use an API to display the Age population, age 14, male
        //from the URL : https://tradingeconomics.com/country-list/age-population-age-14-male-wb-data.html
        router.get("/api/TE/").handler(this::extractData);

        //This router permits to use an API to display the Age population, age 15, male, interpolated
        //from the URL : https://tradingeconomics.com/country-list/age-population-age-15-male-interpolated-wb-data.html
        router.get("/api/TE/").handler(this::extractData);

        //This router permits to use an API to display the Age population, age 16, male, interpolated
        //from the URL : https://tradingeconomics.com/country-list/age-population-age-16-male-interpolated-wb-data.html
        router.get("/api/TE/").handler(this::extractData);

        //This router permits to use an API to display the Age population, age 17, male, interpolated
        //from the URL : https://tradingeconomics.com/country-list/age-population-age-17-male-interpolated-wb-data.html
        router.get("/api/TE/").handler(this::extractData);

        //This router permits to use an API to display the Age population, age 18, male, interpolated
        //from the URL : https://tradingeconomics.com/country-list/age-population-age-18-male-interpolated-wb-data.html
        router.get("/api/TE/").handler(this::extractData);

        //This router permits to use an API to display the Age population, age 19, male, interpolated
        //from the URL : https://tradingeconomics.com/country-list/age-population-age-19-male-interpolated-wb-data.html
        router.get("/api/TE/").handler(this::extractData);

        //This router permits to use an API to display the Age population, age 20, male, interpolated
        //from the URL : https://tradingeconomics.com/country-list/age-population-age-20-male-interpolated-wb-data.html
        router.get("/api/TE/").handler(this::extractData);

        //This router permits to use an API to display the Age population, age 21, male, interpolated
        //from the URL : https://tradingeconomics.com/country-list/age-population-age-21-male-interpolated-wb-data.html
        router.get("/api/TE/").handler(this::extractData);

         //This router permits to use an API to display the Age population, age 22, male, interpolated
        //from the URL : https://tradingeconomics.com/country-list/age-population-age-22-male-interpolated-wb-data.html
        router.get("/api/TE/").handler(this::extractData);

        //This router permits to use an API to display the Age population, age 23, male, interpolated
        //from the URL : https://tradingeconomics.com/country-list/age-population-age-23-male-interpolated-wb-data.html
        router.get("/api/TE/").handler(this::extractData);

        //This router permits to use an API to display the Age population, age 24, male, interpolated
        //from the URL : https://tradingeconomics.com/country-list/age-population-age-24-male-interpolated-wb-data.html
        router.get("/api/TE/").handler(this::extractData);

        //This router permits to use an API to display the Age population, age 25, male, interpolated
        //from the URL : https://tradingeconomics.com/country-list/age-population-age-25-male-interpolated-wb-data.html
        router.get("/api/TE/").handler(this::extractData);

        //This router permits to use an API to display the Annualized average growth rate in per capita real survey mean consumption or income, bottom 40% of population
        //from the URL : https://tradingeconomics.com/country-list/annualized-average-growth-rate-in-per-capita-real-survey-mean-consumption-or-income-bottom-40percent-of-population-wb-data.html
        router.get("/api/TE/").handler(this::extractData);

        //This router permits to use an API to display the Condom use; population ages 15-24; female (% of females ages 15-24)
        //from the URL : https://tradingeconomics.com/country-list/condom-use-population-ages-15-24-female-percent-of-females-ages-15-24-wb-data.html
        router.get("/api/TE/").handler(this::extractData);

        //This router permits to use an API to display the Coverage of unemployment benefits and ALMP in 2nd quintile (% of population)
        //from the URL : https://tradingeconomics.com/country-list/coverage-of-unemployment-benefits-and-almp-in-2nd-quintile-percent-of-population-wb-data.html
        router.get("/api/TE/").handler(this::extractData);

        //This router permits to use an API to display the
        //from the URL :
        router.get("/api/TE/").handler(this::extractData);

        //This router permits to use an API to display the
        //from the URL :
        router.get("/api/TE/").handler(this::extractData);

        //This router permits to use an API to display the
        //from the URL :
        router.get("/api/TE/").handler(this::extractData);

        //This router permits to use an API to display the
        //from the URL :
        router.get("/api/TE/").handler(this::extractData);
        ////////////////////////////////////////////////////////////////////////////////////////////////////////////////
        //Demographics//

        //Economy & Growth//
        ////////////////////////////////////////////////////////////////////////////////////////////////////////////////



        ////////////////////////////////////////////////////////////////////////////////////////////////////////////////
        //Economy & Growth//

        //Energy_&_Mining//
        ////////////////////////////////////////////////////////////////////////////////////////////////////////////////

        ////////////////////////////////////////////////////////////////////////////////////////////////////////////////
        //Energy_&_Mining//

        //External_Debt//
        ////////////////////////////////////////////////////////////////////////////////////////////////////////////////

        ////////////////////////////////////////////////////////////////////////////////////////////////////////////////
        //External_Debt//

        //Gender//
        ////////////////////////////////////////////////////////////////////////////////////////////////////////////////

        ////////////////////////////////////////////////////////////////////////////////////////////////////////////////
        //Gender//

        //Infrastructure//
        ////////////////////////////////////////////////////////////////////////////////////////////////////////////////

        ////////////////////////////////////////////////////////////////////////////////////////////////////////////////
        //Infrastructure//

        //Private_Sector//
        ////////////////////////////////////////////////////////////////////////////////////////////////////////////////

        ////////////////////////////////////////////////////////////////////////////////////////////////////////////////
        //Private_Sector//

        //Public_Sector//
        ////////////////////////////////////////////////////////////////////////////////////////////////////////////////

        ////////////////////////////////////////////////////////////////////////////////////////////////////////////////
        //Public_Sector//

        //Social_Protection_&_Labor//
        ////////////////////////////////////////////////////////////////////////////////////////////////////////////////

        ////////////////////////////////////////////////////////////////////////////////////////////////////////////////
        //Social_Protection_&_Labor//

        //Aid_Effectiveness//
        ////////////////////////////////////////////////////////////////////////////////////////////////////////////////

        ////////////////////////////////////////////////////////////////////////////////////////////////////////////////
        //Aid_Effectiveness//

        //Development//
        ////////////////////////////////////////////////////////////////////////////////////////////////////////////////

        ////////////////////////////////////////////////////////////////////////////////////////////////////////////////
        //Development//

        //Education//
        ////////////////////////////////////////////////////////////////////////////////////////////////////////////////

        ////////////////////////////////////////////////////////////////////////////////////////////////////////////////
        //Education//

        //Environment//
        ////////////////////////////////////////////////////////////////////////////////////////////////////////////////

        ////////////////////////////////////////////////////////////////////////////////////////////////////////////////
        //Environment//

        //Financial_Sector//
        ////////////////////////////////////////////////////////////////////////////////////////////////////////////////

        ////////////////////////////////////////////////////////////////////////////////////////////////////////////////
        //Financial_Sector//

        //Health//
        ////////////////////////////////////////////////////////////////////////////////////////////////////////////////

        ////////////////////////////////////////////////////////////////////////////////////////////////////////////////
        //Health//

        //Poverty//
        ////////////////////////////////////////////////////////////////////////////////////////////////////////////////

        ////////////////////////////////////////////////////////////////////////////////////////////////////////////////
        //Poverty//

        //Projection//
        ////////////////////////////////////////////////////////////////////////////////////////////////////////////////

        ////////////////////////////////////////////////////////////////////////////////////////////////////////////////
        //Projection//

        //Science_&_Technology//
        ////////////////////////////////////////////////////////////////////////////////////////////////////////////////

        ////////////////////////////////////////////////////////////////////////////////////////////////////////////////
        //Science_&_Technology//

        ////////////////////////////////////////////////////////////////////////////////////////////////////////////////

        //News//
        ////////////////////////////////////////////////////////////////////////////////////////////////////////////////

        //This router permits to use an API to display the
        //from the URL :
        router.get("/api/TE/").handler(this::extractData);

        ////////////////////////////////////////////////////////////////////////////////////////////////////////////////
        //News//

        ////////////////////////////////////////////////////////////////////////////////////////////////////////////////

        httpServer.requestHandler(router::accept);

        httpServer.listen(9797, res -> {
            if (res.succeeded())
            {
                startFuture.complete();
            }
            else {
                startFuture.fail(res.cause());
            }
        });
    }
    ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

    //Handlers
    ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

    //Main indicators
    ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

    //This handler permits to extract data
    //from the following URL : https://tradingeconomics.com/country-list/gdp-growth-rate
    private void extractDataGdpGrowthRate(RoutingContext routingContext)
    {
        System.out.println("extractDataGdpGrowthRate executed");
        HttpServerResponse response = routingContext.response();
        response.putHeader("content-type", "application/json");
        response.end(ExtractDataModel1("https://tradingeconomics.com/country-list/gdp-growth-rate"));
    }

    //This handler permits to extract data
    //from the following URL : https://tradingeconomics.com/country-list/interest-rate
    private void extractDataInterestRate(RoutingContext routingContext)
    {
        System.out.println("extractDataInterestRate executed");
        HttpServerResponse response = routingContext.response();
        response.putHeader("content-type", "application/json");
        response.end(ExtractDataModel1("https://tradingeconomics.com/country-list/interest-rate"));
    }

    //This handler permits to extract data
    //from the following URL : https://tradingeconomics.com/country-list/inflation-rate
    private void extractDataInflationRate(RoutingContext routingContext)
    {
        System.out.println("extractDataInflationRate executed");
        HttpServerResponse response = routingContext.response();
        response.putHeader("content-type", "application/json");
        response.end(ExtractDataModel1("https://tradingeconomics.com/country-list/inflation-rate"));
    }

    //This handler permits to extract data
    //from the following URL : https://tradingeconomics.com/country-list/unemployment-rate
    private void extractDataUnemploymentRate(RoutingContext routingContext)
    {
        System.out.println("extractDataUnemploymentRate executed");
        HttpServerResponse response = routingContext.response();
        response.putHeader("content-type", "application/json");
        response.end(ExtractDataModel1("https://tradingeconomics.com/country-list/unemployment-rate"));
    }

    //This handler permits to extract data
    //from the following URL : https://tradingeconomics.com/country-list/government-debt-to-gdp
    private void extractDataGovernmentDebtToGDPRate(RoutingContext routingContext)
    {
        System.out.println("extractDataGovernmentDebtToGDPRate executed");
        HttpServerResponse response = routingContext.response();
        response.putHeader("content-type", "application/json");
        response.end(ExtractDataModel1("https://tradingeconomics.com/country-list/government-debt-to-gdp"));
    }

    //This handler permits to extract data
    //from the following URL : https://tradingeconomics.com/country-list/balance-of-trade
    private void extractDataBalanceOfTradeRate(RoutingContext routingContext)
    {
        System.out.println("extractDataGovernmentDebtToGDPRate executed");
        HttpServerResponse response = routingContext.response();
        response.putHeader("content-type", "application/json");
        response.end(ExtractDataModel1("https://tradingeconomics.com/country-list/balance-of-trade"));
    }

    //This handler permits to extract data
    //from the following URL : https://tradingeconomics.com/country-list/current-account-to-gdp
    private void extractDataCurrentAccountToGDPRate(RoutingContext routingContext)
    {
        System.out.println("extractDataCurrentAccountToGDPRate executed");
        HttpServerResponse response = routingContext.response();
        response.putHeader("content-type", "application/json");
        response.end(ExtractDataModel1("https://tradingeconomics.com/country-list/current-account-to-gdp"));
    }

    ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

    //Markets
    ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

    private void scrapeDataMinimumWages(RoutingContext routingContext)
    {
        System.out.println("scrapeDataTurfooStatistiqueCheval executed");
        HttpServerResponse response = routingContext.response();
        response.putHeader("content-type", "application/json");
        try {
            response.end(minimumWagesDataset());
        } catch (JsonProcessingException e) {
            e.printStackTrace();
        }
    }

    ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

    ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

    //Stop the server.
    ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    @Override
    public void stop(Future stopFuture) throws Exception
    {
        System.out.println("My Server stopped!");
    }
    ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
}