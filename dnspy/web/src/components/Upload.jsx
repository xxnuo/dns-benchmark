import { Tooltip, Button } from "@nextui-org/react";
import { useTranslation } from "react-i18next";
import { useFile } from "../contexts/FileContext";

export default function Upload() {
  const { t } = useTranslation();
  const { setFile, jsonData, setJsonData } = useFile();

  const handleFileChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    const file = event.target.files?.[0];
    if (file) {
      setFile(file);
    }
  };

  const handleClearData = () => {
    setFile(null);
    setJsonData(null);
    localStorage.removeItem("dnsAnalyzerData");
  };

  return (
    <div className="flex gap-2">
      <Tooltip content={t("tip.upload")}>
        <Button color="primary" variant="flat" as="label" className="cursor-pointer">
          <input type="file" className="hidden" accept=".json" onChange={handleFileChange} />
          {t("button.upload")}
        </Button>
      </Tooltip>

      {jsonData && (
        <Tooltip content={t("tip.clear")}>
          <Button color="danger" variant="flat" onClick={handleClearData}>
            {t("button.clear")}
          </Button>
        </Tooltip>
      )}
    </div>
  );
}