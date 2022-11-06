CREATE DATABASE IF NOT EXISTS AdminOnDemand;

USE AdminOnDemand;

CREATE TABLE IF NOT EXISTS Odgovori (
    OdgovorID int NOT NULL UNIQUE AUTO_INCREMENT,
    PRIMARY KEY (OdgovorID),
    Name varchar(50),
    CompanySize varchar(15) NOT NULL,
    AccountingSize varchar(15) NOT NULL,
    CreativeSize varchar(15) NOT NULL,
    ITSize varchar(15) NOT NULL,
    MarketingSize varchar(15) NOT NULL,
    DataStorageSolution varchar(20) NOT NULL,

    CONSTRAINT chk_CompanySize CHECK (CompanySize IN ('micro', 'small', 'medium', 'large')),
    CONSTRAINT chk_AccountingSize CHECK (AccountingSize IN ('0', '1-5', '6-50', '51-250', '>250')),
    CONSTRAINT chk_CreativeSize CHECK (CreativeSize IN ('0', '1-5', '6-50', '51-250', '>250')),
    CONSTRAINT chk_ITSize CHECK (ITSize IN ('0', '1-5', '6-50', '51-250', '>250')),
    CONSTRAINT chk_MarketingSize CHECK (MarketingSize IN ('0', '1-5', '6-50', '51-250', '>250')),
    CONSTRAINT chk_DataStorageSolution CHECK (DataStorageSolution IN ('online', 'local'))
);

CREATE TABLE IF NOT EXISTS Usluge (
    RjesenjeID int NOT NULL UNIQUE AUTO_INCREMENT,
    PRIMARY KEY (RjesenjeID),
    Name varchar(255) NOT NULL,
    Price varchar(30) NOT NULL
);

INSERT INTO Usluge (Name, Price) VALUES ("Microsoft 365 Business Basic", "$6.00");
INSERT INTO Usluge (Name, Price) VALUES ("Microsoft 365 Apps for Business", "$8.25");
INSERT INTO Usluge (Name, Price) VALUES ("Microsoft 365 Business Standard", "$12.50");
INSERT INTO Usluge (Name, Price) VALUES ("Microsoft 365 Business Premium", "$22.00");
INSERT INTO Usluge (Name, Price) VALUES ("Office 365 Enterprise F3", "$4.00");
INSERT INTO Usluge (Name, Price) VALUES ("Office 365 Enterprise E1", "$10");
INSERT INTO Usluge (Name, Price) VALUES ("Office 365 Enterprise E3", "$23");
INSERT INTO Usluge (Name, Price) VALUES ("Office 365 Enterprise E5", "$38");
INSERT INTO Usluge (Name, Price) VALUES ("Microsoft 365 Enterprise F1", "$2.25");
INSERT INTO Usluge (Name, Price) VALUES ("Microsoft 365 Enterprise F3", "$8");
INSERT INTO Usluge (Name, Price) VALUES ("Microsoft 365 Enterprise E3", "$36");
INSERT INTO Usluge (Name, Price) VALUES ("Microsoft 365 Enterprise E5", "$57");
INSERT INTO Usluge (Name, Price) VALUES ("Google Business starter", "$6");
INSERT INTO Usluge (Name, Price) VALUES ("Google Business standard", "$12");
INSERT INTO Usluge (Name, Price) VALUES ("Google Business plus", "$18");
INSERT INTO Usluge (Name, Price) VALUES ("Adobe Creative Cloud", "$55");

