import torch
import torch.nn as nn

def print_iou(iou, acc, miou, macc):
    for ind_class in range(iou.shape[0]):
        print('===> {0:2d} : {1:.2%} {2:.2%}'.format(ind_class, iou[ind_class, 0].item(), acc[ind_class, 0].item()))
    print('mIoU: {:.2%} mAcc : {:.2%} '.format(miou, macc))

def compute_iou(model, testloader):
    model = model.eval()

    interp = nn.Upsample(size=(1024, 2048), mode='bilinear', align_corners=True)
    union = torch.zeros(19, 1,dtype=torch.float).cuda().float()
    inter = torch.zeros(19, 1, dtype=torch.float).cuda().float()
    preds = torch.zeros(19, 1, dtype=torch.float).cuda().float()
    with torch.no_grad():
        for index, batch in tqdm(enumerate(testloader)):
            image, label, _, _, name = batch
            output =  model(image.cuda())
            label = label.cuda()
            output = interp(output).squeeze()
            C, H, W = output.shape
            Mask = (label.squeeze())<C

            pred_e = torch.linspace(0,C-1, steps=C).view(C, 1, 1)
            pred_e = pred_e.repeat(1, H, W).cuda()
            pred = output.argmax(dim=0).float()
            pred_mask = torch.eq(pred_e, pred).byte()
            pred_mask = pred_mask*Mask

            label_e = torch.linspace(0,C-1, steps=C).view(C, 1, 1)
            label_e = label_e.repeat(1, H, W).cuda()
            label = label.view(1, H, W)
            label_mask = torch.eq(label_e, label.float()).byte()
            label_mask = label_mask*Mask

            tmp_inter = label_mask+pred_mask
            cu_inter = (tmp_inter==2).view(C, -1).sum(dim=1, keepdim=True).float()
            cu_union = (tmp_inter>0).view(C, -1).sum(dim=1, keepdim=True).float()
            cu_preds = pred_mask.view(C, -1).sum(dim=1, keepdim=True).float()

            union+=cu_union
            inter+=cu_inter
            preds+=cu_preds

        iou = inter/union
        acc = inter/preds
        mIoU = iou.mean().item()
        mAcc = acc.mean().item()
        print_iou(iou, acc, mIoU, mAcc)
        return iou, mIoU, acc, mAcc
